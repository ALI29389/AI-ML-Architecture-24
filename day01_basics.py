# --- التحدي الأول: حساب العمر ---
age = int(input("Enter your age: "))
years_left = 100 - age
print(f"Years left to reach 100: {years_left}")

# --- التحدي الثاني: القوائم والعمليات ---
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)  # استخدام الدالة التلقائية بدلاً من الجمع اليدوي
max_num = max(numbers)
print(f"Sum: {total_sum}, Max value: {max_num}")

# --- التحدي الثالث: القاموس ---
name_input = input("Enter your name: ")
spec_input = input("Enter your specialization: ")
goal_input = input("Enter your goal: ")

profile = {
    "name": name_input,
    "specialization": spec_input,
    "goal": goal_input
}

print(f"Profile Data: {profile}")
