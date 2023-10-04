from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import  userPost
from app1.forms import  LoginForm, userPostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.

            login(request, user)

            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = {"join_form": join_form}
            return render(request, 'login/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form": join_form}
        return render(request, 'login/join.html', page_data)


def home(request):
    uPost = userPost.objects.filter()
    context = {
            'uPost': uPost,
            'postForm': userPostForm()
        }
    return render(request, 'Home/home.html', context)





# about
def about(request):
    uPost = userPost.objects.filter()
    context = {
        'uPost': uPost,
        'postForm': userPostForm()
    }
    return render(request, 'app1/about.html', context)


def contact(request):
    return render(request, 'MyPosts/myposts.html')  



def additem(request):
    if request.method == "POST":
        if ("add" in request.POST):
            add_form = userPostForm(request.POST, request.FILES)
            if add_form.is_valid():
                description = add_form.cleaned_data["description"]
                category = add_form.cleaned_data["category"]
                itemPhoto = add_form.cleaned_data["itemPhoto"]
                user = User.objects.get(id=request.user.id)
                userPost(user=user, category=category, description=description, itemPhoto=itemPhoto).save()
                return redirect("/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, "Home/additem.html", context)
        else:
            return redirect("/")
    else:
        context = {
            "form_data": userPostForm()
        }
        return render(request, "Home/additem.html", context)


def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                # Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'login/login.html', {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, 'login/login.html', {"login_form": LoginForm})



def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")


