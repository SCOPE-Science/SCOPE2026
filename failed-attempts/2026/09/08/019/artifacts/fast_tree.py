"""Fast DFS enumeration for Av(4123,31524) with O(ls*lp) 31524-check."""
import sys, time

def make_checker():
    def ok(p, pos, m):
        # p: list length m-1, values 1..m-1
        # 4123 via new max: need LIS>=3 in p[pos:]
        # patience with 2 tails
        t1 = 10**9; t2 = 10**9
        for i in range(pos, m-1):
            x = p[i]
            if x < t1:
                t1 = x
            elif x < t2:
                # need x > t1 strictly; if x==t1 impossible (distinct), x>t1 here
                t2 = x
            else:
                # x > t2 > t1
                return False
        # careful: elif x<t2 requires x>t1; since distinct, x<t1 false means x>t1. ok.
        # else branch x>t2. correct LIS>=3 test.
        # 31524: prefix p[:pos], suffix p[pos:]
        lp = pos; ls = m-1-pos
        if lp >= 2 and ls >= 2:
            # suffix max array: smax[j] = max(p[pos+j+1:])
            # iterate j1 from end
            curmax = -1
            # we need for each j1: w1=p[pos+j1], w2max=max after j1
            # loop backwards maintaining curmax
            # also need prefix scan per j1; build prefix suffix-min once
            # sufmin[i] = min(p[i+1..lp-1]) for i in [0,lp)
            # compute on demand
            sufmin = [0]*lp
            sm = 10**9
            for i in range(lp-1, -1, -1):
                sufmin[i] = sm
                if p[i] < sm: sm = p[i]
            for j1 in range(ls-1, -1, -1):
                w1 = p[pos+j1]
                if curmax > w1:
                    w2 = curmax
                    # scan prefix for i with w1 < p[i] < w2 and sufmin[i] < w1
                    for i in range(lp):
                        v = p[i]
                        if w1 < v < w2 and sufmin[i] < w1:
                            return False
                if w1 > curmax: curmax = w1
        return True
    return ok

OK = make_checker()

def count_dfs(nmax):
    counts = [0]*(nmax+1)
    counts[0] = 1
    # iterative DFS: stack of (perm_list, next_m_to_expand...) — instead level-by-level
    # Use explicit stack of lists; expand depth-first.
    # counts[m] = number of nodes at depth m.
    stack = [[]]  # start with empty perm (length 0)
    # We do DFS: pop node of length L; if L>0 it was already counted when pushed.
    # Push children of length L+1.
    # To keep stack small, push in reverse.
    while stack:
        node = stack.pop()
        L = len(node)
        if L == nmax:
            continue
        m = L+1
        # find valid positions
        for pos in range(m-1, -1, -1):
            if OK(node, pos, m):
                child = node[:pos] + [m] + node[pos:]
                counts[m] += 1
                stack.append(child)
    return counts

def count_level_bfs(nmax):
    cur = [[]]
    counts = [1]+[0]*nmax
    for m in range(1, nmax+1):
        nxt = []
        for p in cur:
            for pos in range(m):
                if OK(p, pos, m):
                    nxt.append(p[:pos]+[m]+p[pos:])
        counts[m] = len(nxt)
        cur = nxt
        print(f"n={m}: {counts[m]}", flush=True)
    return counts

if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv)>1 else 10
    mode = sys.argv[2] if len(sys.argv)>2 else "dfs"
    t0=time.time()
    if mode=="dfs":
        c = count_dfs(nmax)
        print(c, flush=True)
    else:
        c = count_level_bfs(nmax)
        print(c, flush=True)
    print("time", time.time()-t0, flush=True)
