from django.shortcuts import render,redirect
from.forms import Registrationform,userupdateform,profileupdateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register(request):
    if request.method=='POST':
      form=Registrationform(request.POST)
      if form.is_valid():
       form.save()
       username=form.cleaned_data.get('username')
       messages.success(request,f'you are successfully registered {username}')
       return redirect('login')
    else:
      form=Registrationform()

    return render(request,'User/register.html',{'form':form})

def logout_users(request):
  messages.success(request,'you have logged out succesfully!')
  logout(request)
  return redirect('login')

@login_required
def profile(request):
  return render (request,'User/profile.html')


@login_required
def profile_update(request):
  if request.method=='POST':
    u_form=userupdateform(request.POST,instance=request.user)
    p_form=profileupdateform(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,'profile updated succesfully')
      return redirect('profile')
  else:
    u_form=userupdateform(instance=request.user)
    p_form=profileupdateform(instance=request.user.profile)
  
  context={
    "u_form":u_form,
    "p_form":p_form
  }
  return render (request,'User/profile_update.html',context)
