"""Script AAcap: SOUND (over-approximating) exact-depth enumeration for the W-star lemma.
States for non-x0 vertices: A (depth 0, V1^(0)\\{x0}), or exact depth d in 1..L, with L
meaning 'depth >= L' (cap). Edge rules (over-approx => sound for proving ABSENCE):
 - Window with x0 (exactly once; twice impossible for distinct verts):
   B: other two = (A, deeper>=1) [pair {x0,A} at depth 0 + third deeper]. Deeper check
      with cap: A=0, d>=1 (cap L counts as deep). Exact.
   S: other two both depth EXACTLY 1 (W = V1^(1)). Cap L>=2 never W. Exact.
   Note {x0, A1, A2} (both depth 0): not edge. {x0,W,D}: B? pair {x0,W}: W at depth1,
      need third... B needs TWO at same depth d + third deeper: {x0,W,D}: depths (0,1,e):
      no equal pair -> NOT edge. Correct (matches scriptQ).
 - Window without x0, depths (t1,t2,t3) with cap: B-edge iff two mins equal, third deeper.
   With cap value L: if sorted (a,b,c) has a==b<c -> edge (sound: cap only inflates c... if
   c==L true depth>=L>b: still deeper -> edge, sound). If (b==c==L, a<b): true depths could
   be (d,d,e) equal-pair-deep + ... : triple like (a, L1, L2) with L1,L2>=L: if L1==L2 (same
   exact depth): equal pair is MAX -> not edge; if differ -> no pair -> not edge. Either way
   NOT edge: sound to return False. If (L,L,L) all-cap: ambiguous (could be (e,e,f) true edge
   or (e,e,e) non-edge or (e,f,g)) -> return TRUE (over-approx, sound direction).
   All other triples exact (no cap involved): standard rule.
If ZERO words with >=1 star window and all windows edges -> lemma holds for ALL n.Else inspect."""
import itertools

L = 6  # depths 1..L-1 exact, L = '>=L'
A = 0  # V1 rest

def edge_nox0(t):
    s = tuple(sorted(t))
    a, b, c = s
    if a == b and c > b:
        return True
    if a == b == c == L:
        return True  # over-approx of deep ambiguity (sound direction)
    return False

def edge_x0(o1, o2):
    # others o1,o2 in {A=0} U {1..L}; B: one is A(0), other >=1; S: both == 1
    B = (o1 == A and o2 >= 1) or (o2 == A and o1 >= 1)
    S = (o1 == 1 and o2 == 1)
    return B or S

# sanity
assert edge_x0(A, 1) and edge_x0(A, L) and edge_nox0((1, 1, 2))
assert not edge_x0(1, 1) or True  # {x0,W,W} star True actually
assert edge_x0(1, 1)  # star
assert not edge_x0(A, A) and not edge_x0(1, 2) and not edge_nox0((1, 2, 2))
assert not edge_nox0((0, 0, 0)) and edge_nox0((0, 0, 1))
print("sanity OK")

states = [A] + list(range(1, L + 1))
surv = []
for rest in itertools.product(states, repeat=6):
    w = (999,) + rest  # 999 = x0 marker
    wins = [(w[i], w[(i + 1) % 7], w[(i + 2) % 7]) for i in range(7)]
    has_star = False
    ok = True
    for win in wins:
        nx = win.count(999)
        if nx == 0:
            if not edge_nox0(win):
                ok = False; break
        elif nx == 1:
            o = [s for s in win if s != 999]
            if not edge_x0(o[0], o[1]):
                ok = False; break
            if o[0] == 1 and o[1] == 1:
                has_star = True
        else:
            ok = False; break
    if ok and has_star:
        surv.append(w)
print("surviving words (sound over-approx):", len(surv))
for w in surv[:30]:
    print("  ", w)
# report whether survivors rely on (L,L,L) over-approx windows
if surv:
    dep = sum(1 for w in surv if any(
        w[i] != 999 and w[(i+1)%7] != 999 and w[(i+2)%7] != 999 and
        tuple(sorted((w[i], w[(i+1)%7], w[(i+2)%7]))) == (L, L, L) for i in range(7)))
    print("of which using (L,L,L)-windows:", dep)
