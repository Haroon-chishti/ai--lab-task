def fizzbuzz_interactive(n=100):
    score=0
    attempts=0
    for i in range(1, n+1):
        correct = "FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i)
        ans = input(f"{i}: ").strip()
        if not ans:
            print("Empty input"); continue
        if ans.lower() in ("q","quit"):
            break
        attempts += 1
        if ans.lower() == correct.lower():
            score += 1; print("Correct")
        else:
            print("Wrong. Expected:", correct)
    print(f"Score: {score}/{attempts}")

if __name__ == "__main__":
    try:
        n_input = input("Max number (default 100): ").strip()
        n = int(n_input) if n_input else 100
    except:
        n = 100
    fizzbuzz_interactive(n)