"""Script O: refined depth-word check with full depth alphabet {0,1,2,3}
(2+ levels distinguished), star still {0,1,1}. Also allow B-type across any equal pair."""
import itertools

def allowed(t):
    s = tuple(sorted(t))
    a, b, c = s
    if len(set(s)) == 1:
        return False
    if (a == b and c > b) or (b == c and a < b):
        return True
    if s == (0, 1, 1):
        return True
    return False

for D in [3, 4]:
    surv = []
    for w in itertools.product(range(D), repeat=7):
        wins = [tuple(sorted((w[i], w[(i+1)%7], w[(i+2)%7]))) for i in range(7)]
        if not any(x == (0, 1, 1) for x in wins):
            continue
        if all(allowed(x) for x in wins):
            surv.append(w)
    print(f"D={D}: surviving words with star-window: {len(surv)}")
    for w in surv[:20]:
        print("  ", w)
