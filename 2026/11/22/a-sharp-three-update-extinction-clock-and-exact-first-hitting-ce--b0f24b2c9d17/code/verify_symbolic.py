"""Independent coefficient method for first extinction times on quadrilateral books.
No third-party packages. Counts use only local nine-state arm enumerations.
"""
from collections import defaultdict

def count_no_new_excitation(m):
    count = 0
    for h in (0, 1, 2):
        for j in (0, 1, 2):
            polynomial = defaultdict(int)
            # A page pair contributes a monomial recording initially excited arms.
            for a in (0, 1, 2):
                for b in (0, 1, 2):
                    if a == 0 and h == 1 and b == 1: continue
                    if b == 0 and j == 1 and a == 1: continue
                    polynomial[(int(a == 1), int(b == 1))] += 1
            state = {(0, 0): 1}
            # For a hub that is initially resting, its excited neighbors may
            # include at most one in total, including the opposite hub.
            hi = (1 - int(j == 1)) if h == 0 else m
            hj = (1 - int(h == 1)) if j == 0 else m
            if hi < 0 or hj < 0: continue
            for _ in range(m):
                nxt = defaultdict(int)
                for (i,k),w in state.items():
                    for (di,dk),r in polynomial.items():
                        if i+di <= hi and k+dk <= hj:
                            nxt[(i+di,k+dk)] += w*r
                state = nxt
            count += sum(state.values())
    return count

def closed_form(m):
    return (9**m+7**m+2*8**m+4*6**m+6*m*6**(m-1)
            +(m+2)**2*4**(m-1))

if __name__ == '__main__':
    # This method contains neither the full graph transition map nor direct trajectories.
    for m in range(1,31):
        got = count_no_new_excitation(m)
        expected = closed_form(m)
        assert got == expected, (m,got,expected)
        assert 4**(m+1) < got < 9**(m+1)
        if m <= 8 or m in (12,20,30):
            print(f'm={m} initial_states={9**(m+1)} F2_all_rest={got} exact_P_tau3={(9**(m+1)-got)}/{9**(m+1)} PASS')
    print('30 symbolic parameter cases PASS')
