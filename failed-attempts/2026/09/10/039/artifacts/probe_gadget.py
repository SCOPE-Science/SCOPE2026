import itertools


def ind3(x, y):
    y0 = y & 1
    y1 = (y >> 1) & 1
    return y0 if x == 0 else y1


M = [[ind3(x, y) for y in range(4)] for x in range(2)]
print("IND_3 matrix rows x=0,1; cols y=00,01,10,11:")
for r in M:
    print(r)

# rank over floats (2x4, trivial)
def rank_mat(mat):
    m = [list(map(float, r)) for r in mat]
    R = len(m)
    C = len(m[0])
    row = 0
    r = 0
    for c in range(C):
        piv = None
        for i in range(row, R):
            if abs(m[i][c]) > 1e-9:
                piv = i
                break
        if piv is None:
            continue
        m[row], m[piv] = m[piv], m[row]
        for i in range(R):
            if i != row and abs(m[i][c]) > 1e-9:
                f = m[i][c] / m[row][c]
                for j in range(c, C):
                    m[i][j] -= f * m[row][j]
        row += 1
        r += 1
    return r


print("rank(IND_3) =", rank_mat(M))
print("D(IND_3) = 1 (Alice sends 1-bit pointer)")

best = 0
bestR = None
for am in range(1, 4):
    for bm in range(1, 16):
        A = [x for x in range(2) if am >> x & 1]
        B = [y for y in range(4) if bm >> y & 1]
        s = sum(1 if ind3(x, y) == 0 else -1 for x in A for y in B)
        d = abs(s) / 8
        if d > best:
            best = d
            bestR = (A, B, s)
print("discrepancy(uniform) =", best, "witness", bestR)

mx = 0
for am in range(1, 4):
    for bm in range(1, 16):
        A = [x for x in range(2) if am >> x & 1]
        B = [y for y in range(4) if bm >> y & 1]
        vs = set(ind3(x, y) for x in A for y in B)
        if len(vs) == 1:
            mx = max(mx, len(A) * len(B) / 8)
print("largest monochromatic rectangle fraction =", mx)
print("VERIFY_DATA rank=2 D=1")
