# ایجاد یک فهرست برای ذخیره کاربرانی که ورودی را پر کرده‌اند
user_entries = []

while True:
    user_input = input("لطفاً ورودی خود را وارد کنید (یا برای خروج از برنامه خالی بگذارید): ")

    # اگر کاربر ورودی خالی بگذارد، برنامه خاتمه می‌یابد
    if not user_input:
        break

    # افزودن ورودی به فهرست کاربران
    user_entries.append(user_input)

# نمایش تمام کاربرانی که ورودی را پر کرده‌اند
if user_entries:
    print("کاربرانی که ورودی را پر کرده‌اند:")
    for user_entry in user_entries:
        print(user_entry)
else:
    print("هیچ کاربری ورودی را پر نکرده است.")
