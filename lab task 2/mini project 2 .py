movies=[("Eternal Sunshine of the Spotless Mind",20000000),("Memento",9000000),("Requiem for a Dream",45000000),("Pirates of the Caribbean: On Stranger Tides",379000000),("Avengers: Age of Ultron",365000000),("Avengers: Endgame",356000000),("Incredibles 2",200000000)]
def get_positive_int(prompt):
    while True:
        try:
            v=int(input(prompt).strip())
            if v<0:
                continue
            return v
        except:
            pass
def get_nonempty(prompt):
    while True:
        s=input(prompt).strip()
        if s:
            return s
n=get_positive_int("How many movies do you want to add? Enter 0 for none: ")
for _ in range(n):
    title=get_nonempty("Movie title: ")
    budget=get_positive_int("Budget (USD, integer): ")
    movies.append((title,budget))
avg=sum(b for _,b in movies)/len(movies)
print(f"Average budget: ${avg:,.2f}")
above=[(t,b,b-avg) for t,b in movies if b>avg]
for t,b,d in above:
    print(f"{t} is above average by ${d:,.2f} (budget=${b:,.0f})")
print(f"Number of movies above average: {len(above)}")