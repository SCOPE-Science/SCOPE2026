"""Direct independent finite-state verification for sequential open-neighborhood NOR on cycles."""

def sweep(state, n):
    for i in range(n):
        left = (state >> ((i-1) % n)) & 1
        right = (state >> ((i+1) % n)) & 1
        nxt = int((left | right) == 0)
        state = (state & ~(1 << i)) | (nxt << i)
    return state


def no_adjacent_and_dominating(state, n):
    for i in range(n):
        left=(state >> ((i-1) % n))&1
        here=(state >> i)&1
        right=(state >> ((i+1) % n))&1
        if here and (left or right):
            return False
        if not (left or here or right):
            return False
    return True


def main():
    R = {3:8, 4:10, 5:26}
    P = {3:3, 4:2, 5:5}
    for n in range(6,17):
        R[n]=2*R[n-2]+2*R[n-3]
        P[n]=P[n-2]+P[n-3]
    for n in range(3,17):
        census=[0,0,0]
        for state in range(1<<n):
            s1=sweep(state,n)
            s2=sweep(s1,n)
            assert sweep(s2,n)==s2, ('two-sweep bound',n,state)
            assert no_adjacent_and_dominating(s2,n)
            time=0 if state==s1 else (1 if s1==s2 else 2)
            census[time]+=1
            assert (time==0)==(state==s1)
        assert census==[P[n],R[n]-P[n],(1<<n)-R[n]], (n,census)
        print(n,*census)
    print('direct exhaustive checks passed')
if __name__=='__main__':main()
