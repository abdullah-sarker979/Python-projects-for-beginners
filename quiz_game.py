# Simple 10-Question Quiz Program

score = 0
print("🔥 Welcome to the Ultimate Quiz! 🔥\n")

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()
if answer == "paris":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Paris.")

# Question 2
answer = input("\n2. What is 5 + 7? ").strip()
if answer == "12":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is 12.")

# Question 3
answer = input(
    "\n3. Who developed Python programming language? ").strip().lower()
if answer in ["guido van rossum", "guido"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Guido van Rossum.")

# Question 4
answer = input(
    "\n4. What is the largest planet in our Solar System? ").strip().lower()
if answer == "jupiter":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Jupiter.")

# Question 5
answer = input(
    "\n5. What language is primarily used for web styling? ").strip().lower()
if answer == "css":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is CSS.")

# Question 6
answer = input("\n6. What does CPU stand for? ").strip().lower()
if answer in ["central processing unit", "central processor unit"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Central Processing Unit.")

# Question 7
answer = input(
    "\n7. Who wrote the famous book 'Harry Potter'? ").strip().lower()
if answer in ["j.k. rowling", "jk rowling", "rowling"]:
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is J.K. Rowling.")

# Question 8
answer = input("\n8. What is the chemical symbol for water? ").strip().lower()
if answer == "h2o":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is H2O.")

# Question 9
answer = input(
    "\n9. Which continent is the Sahara Desert located in? ").strip().lower()
if answer == "africa":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is Africa.")

# Question 10
answer = input("\n10. What year did World War II end? ").strip()
if answer == "1945":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong! The correct answer is 1945.")

# Final Score
print(f"\nYour total score: {score}/10")

# Performance feedback
if score == 10:
    print("🏆 Perfect! You’re a genius!")
elif score >= 7:
    print("🔥 Great job! You know your stuff.")
elif score >= 4:
    print("👍 Not bad! Keep learning.")
else:
    print("😕 You need more practice — go again!")
