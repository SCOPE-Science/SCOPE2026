import random, math, json, time

def compose(p, q):
    # apply q then p (right-to-left), tuples on {0..n-1}
    return tuple(p[q[i]] for i in range(len(p)))

def pw(p, k):
    n = len(p); r = tuple(range(n)); b = p[:]
    k = k % math.lcm(*[1]) if False else k
    e = k
    base = list(p)
    # binary power
    res = list(range(n))
    while e:
        if e & 1: res = [base[res[i]] if False else base[i] for i in [0]*0] or res
        e >>= 1
    # simpler: repeated (orders small)
    res = list(range(n))
    for _ in range(k % order(p)):
        res = [p[res[i]] for i in range(n)]
    return tuple(res)

def order(p):
    n = len(p); seen = list(range(n)); cur = list(range(n)); k = 0
    while True:
        cur = [p[cur[i]] for i in range(n)]; k += 1
        if all(cur[i]==i for i in range(n)): return k
        if k > 200: return -1

def comm(a, b):
    n = len(a); ai = inv(a); bi = inv(b)
    return compose(compose(compose(a, b), ai), bi)

def inv(p):
    n = len(p); q = [0]*n
    for i in range(n): q[p[i]] = i
    return tuple(q)

def is_id(p): return all(p[i]==i for i in range(len(p)))

def w(a, b, s):
    return comm(pw(a, s), pw(b, s))

def rand_perm(n):
    l = list(range(n)); random.shuffle(l); return tuple(l)

def perm_of_cycles(n, cycles):
    p = list(range(n))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i+1) % len(c)]
    return tuple(p)

out = {}
# (a) S3 separator for S={2,3} -> N=5
A = perm_of_cycles(3, [[0,1]]); B = perm_of_cycles(3, [[0,1,2]])
out['S3'] = {'ordA': order(A), 'ordB': order(B),
             'w2': is_id(w(A,B,2)), 'w3': is_id(w(A,B,3)),
             'w5_nontrivial': not is_id(w(A,B,5))}
# (c) S3 for {6,10,15} -> 7
out['S3_6_10_15'] = {'w6': is_id(w(A,B,6)), 'w10': is_id(w(A,B,10)),
                     'w15': is_id(w(A,B,15)),
                     'w7_nontrivial': not is_id(w(A,B,7))}
# S={4,9} -> 5
out['S3_4_9'] = {'w4': is_id(w(A,B,4)), 'w9': is_id(w(A,B,9)),
                 'w5_nontrivial': not is_id(w(A,B,5))}

# (b) Heisenberg UT3(Z_n): A=E12(1), B=E23(1); [A^s,B^s]=E13(s^2)
def heis(n, s):
    return (s*s) % n == 0
out['heis_S46_mod4'] = {'kill4': heis(4,4), 'kill6': heis(4,6),
                        'preserve3': heis(4,3) is False}
out['heis_S69_mod9'] = {'kill6': heis(9,6), 'kill9': heis(9,9),
                        'preserve5': heis(9,5) is False}

# (d) bounded random search for {2,3,5} -> 7 separator in S_10
random.seed(1175)
t0 = time.time(); tested = 0; cover_ok = 0; found = None
while time.time()-t0 < 75:
    n = 10
    a = rand_perm(n); b = rand_perm(n)
    oa, ob = order(a), order(b)
    tested += 1
    # necessary covering condition
    if not all(math.gcd(s, oa) > 1 or math.gcd(s, ob) > 1 for s in (2,3,5)):
        continue
    cover_ok += 1
    if is_id(w(a,b,2)) and is_id(w(a,b,3)) and is_id(w(a,b,5)) and not is_id(w(a,b,7)):
        found = {'A': list(a), 'B': list(b), 'ordA': oa, 'ordB': ob}
        break
out['search_235'] = {'tested': tested, 'cover_ok': cover_ok,
                     'found': found is not None,
                     'example': found,
                     'time_s': round(time.time()-t0,1)}
print(json.dumps(out, indent=1))
