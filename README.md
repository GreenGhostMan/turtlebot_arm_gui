<h5>turtlebot_arm_gui</h5>

ဒီ package ထဲက start.launch ကိုအသုံးပြုပီး turtlebot arm ကို gui ကနေ command ပေးနိုင်မှာဖြစ်ပါသည်
အလုပ်လုပ်ပုံကတော့ 
၁) dynamixel အတွက် controller.launch
၂) camera အတွက် astra.launch ( သင့်မှာရှိတဲ့ camera driver အရ ပြင်ပါ )
၃) arm ကို camera က နေကြည့်ဖို့ image_view node
၄) slider တွေရဲ့ label value တွေကိုကြည့်ပီး သက်ဆိုင်ရာ parameter များကို set လုပ်ပေးတဲ့ GUI ပါတဲ့ arm_controller.py
၅) parameter တွေကိုဖတ်ပီး joint command တွေကိုထုတ်ပေးနေတဲ့ publisher.cpp
