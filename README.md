<h5>turtlebot_arm_gui</h5>

ဒီ package ထဲက start.launch ကိုအသုံးပြုပီး turtlebot arm ကို gui ကနေ command ပေးနိုင်မှာဖြစ်ပါသည် <br>
အလုပ်လုပ်ပုံကတော့ <br>
၁) dynamixel အတွက် controller.launch <br>
၂) camera အတွက် astra.launch ( သင့်မှာရှိတဲ့ camera driver အရ ပြင်ပါ ) <br>
၃) arm ကို camera က နေကြည့်ဖို့ image_view node <br>
၄) slider တွေရဲ့ label value တွေကိုကြည့်ပီး သက်ဆိုင်ရာ parameter များကို set လုပ်ပေးတဲ့ GUI ပါတဲ့ arm_controller.py <br>
၅) parameter တွေကိုဖတ်ပီး joint command တွေကိုထုတ်ပေးနေတဲ့ publisher.cpp <br>
