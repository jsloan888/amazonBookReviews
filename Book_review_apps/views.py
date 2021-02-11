from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request,'index.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_reviews": Book.objects.all(),
        "all_comments": Comment.objects.all()
    }
    return render(request, 'success.html', context)
        

def register(request):
    errors = User.objects.reg_val(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(
        ), bcrypt.gensalt()).decode()  # to encode the password from the form

        new_user = User.objects.create(
            f_name=request.POST['f_name'], l_name=request.POST['l_name'], email=request.POST['email'], password=hashed_pw)
        request.session['user_id'] = new_user.id
        return redirect('/success')


def login(request):
    errors = User.objects.log_val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect('/')
    else:
        existing = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = existing.id
        return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request, userid):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=userid),
        'reviews' : Book.objects.all()
    }
    return render(request, 'profile.html', context)

def new(request, userid):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'new.html', context)

def reviewEdit(request, bookid):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'review' : Book.objects.filter(posted_by=request.session['user_id'])
    }
    return render(request, 'reviewEdit.html', context)

def createReview(request, userid):
    user = User.objects.get(id=userid)
    if request.method == 'POST':
        book = Book.objects.create(
           title=request.POST['name'],
           description=request.POST['desc'],
           posted_by=user
        )
        return redirect(f'/profile/{userid}')
    return redirect('/')

#do we need to add timestamp to views?

def editReview(request,bookid):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == 'GET':
        context = {
            'book_review' : Book.objects.get(id=bookid)
        }
        return render(request, 'reviewEdit.html', context)
    review = Book.objects.get(id=bookid)
    if review.posted_by.id == request.session['user_id']:
        review.title = request.POST['title']
        review.description = request.POST['description']
        review = review.save()
    return redirect(f"/profile/{request.session['user_id']}")
     
def deletereview(request,bookid):
    if 'user_id' not in request.session:
        return redirect('/')
    review = Book.objects.get(id=bookid)
    if review.posted_by.id == request.session['user_id']:
        review.delete()
    return redirect(f"/profile/{request.session ['user_id']}")

def comment(request, userid, bookid):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=userid)
    if request.method == 'POST':
        posted_comment = Comment.objects.create(
           content=request.POST['comment_content'],
           review=Book.objects.get(id=bookid),
           poster=user
        )
        return redirect('/success')
    return redirect('/')

# def likeComment(request, userid, bookid):
#     liked_comment = Comment.objects.get(id=bookid)
#     liked_comment.liked_by = request.session['userid']
#     liked_comment.save()
#     return redirect(f'profile/{userid}')

# def deleteComment(request, userid, commentid):
#     if 'userid' not in request.session:
#         return redirect('/')
#     comment = Comment.objects.get(id=commentid)
#     if comment.posted_by.id == request.session['userid']:
#         comment.delete()
#     return redirect(f'profile/{userid}')