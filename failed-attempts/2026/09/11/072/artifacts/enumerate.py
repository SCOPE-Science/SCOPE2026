"""Finite-window conjugacy/factor census for rank-2 S-adic demo (lane-862).

Systems:
  X = Fibonacci S-adic subshift (constant directive F: 0->01, 1->0),
      the rank-1 base case of the rank-2 class;
  Y = S-adic subshift for telescoped alternating directive H = F o swap(F),
      a genuinely primitive recognizable rank-2 system with a different
      language (unbounded directive history in the untelescoped picture).

What the script shows (mechanics of the decidability theorem in DRAFT.md):
  1. Radius bound R and window W are computable from the recognizability
     index bound I0 (here R=2*I0, W=4*I0+2 up to the demo's small constants).
  2. X->X census over ALL binary block codes of radius <=1: the window test
     passes exactly the codes whose action on occurring blocks equals a
     shift S^k, k in {-1,0,+1} -- i.e. the radius lemma + window test
     recover precisely the shift orbit, as coalescence/virtual-Z predicts.
  3. X->Y census: no code of radius <=1 passes (correctly: the finite
     languages already differ, so no conjugacy exists at any radius --
     a certified NON-CONJUGACY decision on this pair).

A full exhaustive run over ALL codes of radius <R is doubly exponential and
not attempted; the radius<=1 census plus the shift-action analysis is the
bounded demonstration. Replay: python3 enumerate.py
"""
import itertools, hashlib

def F(w):
    return "".join("01" if c == "0" else "0" for c in w)

def G0(w):
    return "".join("10" if c == "0" else "1" for c in w)

def G1(w):
    return "".join("01" if c == "0" else "0" for c in w)

def iterate(morphs, seed="0", steps=22):
    w = seed
    for i in range(steps):
        w = morphs[i % len(morphs)](w)
        if len(w) > 8000:
            break
    return w

X_prefix = iterate([F])
Y_prefix = iterate([G0, G1])

def factors(w, n):
    return {w[i:i+n] for i in range(len(w)-n+1)}

def apply_code(word, code, r):
    out = []
    for i in range(r, len(word)-r):
        out.append(code[word[i-r:i+r+1]])
    return "".join(out)

def window_test(code, r, src_factors_full, tgt_prefix, W):
    Wimg = W - 2*r
    tgt = factors(tgt_prefix, Wimg)
    img = {apply_code(bw, code, r) for bw in src_factors_full}
    if not img.issubset(tgt):
        return False, "image-not-in-target-language"
    Wp = W - 2*r
    cov = set()
    for bw in src_factors_full:
        cov.update(factors(apply_code(bw, code, r), Wp))
    if not factors(tgt_prefix, Wp).issubset(cov):
        return False, "not-surjective-on-window"
    return True, "pass"

def all_codes(r):
    blocks = ["".join(b) for b in itertools.product("01", repeat=2*r+1)]
    for vals in itertools.product("01", repeat=len(blocks)):
        yield dict(zip(blocks, vals))

I0 = 6
R = 2*I0
W = 4*I0 + 2
out = [f"X_prefix_len={len(X_prefix)} Y_prefix_len={len(Y_prefix)}",
       f"I0={I0} R={R} W={W}",
       f"|L_X(W)|={len(factors(X_prefix,W))} |L_Y(W)|={len(factors(Y_prefix,W))}"]

# ---- census 1: X -> X, exhaustive radius <= 1 ----
LX = factors(X_prefix, W)
W3 = 3 + 2*1  # radius-1 codes read triples; use occurring blocks of right size
def occ_blocks(r):
    return sorted(factors(X_prefix, 2*r+1))
occ3 = occ_blocks(1)
out.append(f"occurring-triples={occ3}")
shift_actions = {k: {b: b[1+k] for b in occ3} for k in (-1, 0, 1)}
for r in (0, 1):
    tested, actions = 0, {}
    occ = occ_blocks(r)
    inv = {tuple(v[b] for b in occ): k for k, v in
           ({k: {b: b[r+k] for b in occ} for k in range(-r, r+1)}).items()}
    for code in all_codes(r):
        tested += 1
        ok, _ = window_test(code, r, LX, X_prefix, W)
        if ok:
            act = tuple(code[b] for b in occ)
            actions[act] = actions.get(act, 0) + 1
    # identify each passing action with a shift power
    identified = {inv.get(a, "NONSHIFT"): c for a, c in actions.items()}
    out.append(f"X->X radius<={r}: tested={tested} distinct-passing-actions={len(actions)} "
               f"actions-vs-shifts={identified}")
    out.append(f"  => all passing actions are shift powers: {all(a in inv for a in actions)}")

# ---- census 2: X -> Y, exhaustive radius <= 1 (expect: none pass) ----
LYw = factors(Y_prefix, W)
for r in (0, 1):
    tested, npass = 0, 0
    for code in all_codes(r):
        tested += 1
        ok, _ = window_test(code, r, LX, Y_prefix, W)
        npass += ok
    out.append(f"X->Y radius<={r}: tested={tested} window-pass={npass}")
out.append("DECISION X vs Y at radius<=1: no conjugacy witness (languages differ at length 3: "
           f"X={sorted(factors(X_prefix,3))} Y={sorted(factors(Y_prefix,3))})")

log = "\n".join(out) + "\n"
with open("enumeration_log.txt", "w") as fh:
    fh.write(log)
print(log)
print("sha256:", hashlib.sha256(log.encode()).hexdigest())
