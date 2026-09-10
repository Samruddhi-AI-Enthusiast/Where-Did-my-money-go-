from analyzer import analyze_expenses

print("💸 WHERE DID MY MONEY GO? 💸")

budget = float(input("\nEnter your monthly budget: ₹"))

expenses = {}

print("\nEnter your expenses:")

expenses["Food"] = float(input("Food: ₹"))
expenses["Travel"] = float(input("Travel: ₹"))
expenses["Shopping"] = float(input("Shopping: ₹"))
expenses["Entertainment"] = float(input("Entertainment: ₹"))

total, biggest = analyze_expenses(expenses)

remaining = budget - total

print("\n----------------------------")
print("📊 EXPENSE SUMMARY")
print("----------------------------")

print(f"💰 Total spent: ₹{total:.2f}")
print(f"🔥 Biggest expense: {biggest}")
print(f"💵 Remaining budget: ₹{remaining:.2f}")

if remaining < 0:
    print("⚠️ You have exceeded your budget!")
else:
    print("✅ You are within your budget!")

print("----------------------------")