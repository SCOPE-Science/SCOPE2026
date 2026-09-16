"""Script P: strengthen using VERTEX IDENTITY, not just depths.
Surviving depth-words all contain >=2 zeros (x0 appears once? no—multiple depth-0 verts).
Refine: track (a) whether the depth-0 vertex in each window equals x0 or another V1 vertex;
(b) x0's link: x0-links only to {y in V1, w deeper} pairs and star pairs {w1,w2 in W}.
Key structural fact: star windows MUST contain x0 (only x0 participates in star edges).
So EVERY star-window contains the distinguished vertex x0. Depth-word analysis with
distinguished x0: enumerate assignments (pos of x0 + depths of others) and check windows:
 - window containing x0 + 2 others {a,b}: edge iff ({a,b} both in V1\{x0}? NO:
   B needs pair {x0,y},y in V1 + third deeper; or {a,b}={w1,w2} both in W (star)).
   So window {x0, y in V1, w' }: B-edge iff w' deeper — YES if w' in V2.
   Window {x0, w1, w2}: edge iff (w1 in V1 and w2 in V2) [B] or (both in W) [star];
   NOT an edge if e.g. both in V2\W, or one in V1 one in... check.
 - window NOT containing x0: B-rule only.
Enumerate: positions 0..6, x0 at position 0 wlog (rotation), depths in {0,1,2,3} for
others with V1/W/V2身份 distinguished: state per vertex in {X0, A (V1\{x0}), W, D (V2\W deep)}.
Check all 4^6*... assignments: which cyclic words have all 7 windows edges with >=1 star window?
If ZERO -> sharpness lemma PROVED (need also handle star window with x0 + 2 W's: the only
star type; B-windows with x0 need care)."""
import itertools

# states: 0=X0, 1=A(V1 rest), 2=W, 3=D(deep V2\W, depth>=2)
def inV1(s): return s in (0, 1)
def inW(s): return s == 2

def edge(u, v, w):
    states = (u, v, w)
    nx0 = states.count(0)
    others = [s for s in states if s != 0]
    if nx0 == 0:
        # B-rule on depths: map A->0, W->1, D->2
        d = {1: 0, 2: 1, 3: 2}
        t = tuple(sorted(d[s] for s in states))
        a, b, c = t
        if len(set(t)) == 1: return False
        return (a == b and c > b) or (b == c and a < b)
    if nx0 >= 2:
        return False  # {x0,x0,.} impossible (distinct verts); two V1-zeros need third deeper but x0 twice impossible
    a, b = others
    # B-edges through x0: pair {x0, y}: y must be in V1 (A), third deeper (W or D)
    # here pair containing x0 is (x0,a) or (x0,b): valid iff (a in V1 and b deeper) or (b in V1 and a deeper)
    def deeper(s): return s in (2, 3)
    B = (inV1(a) and a != 0 and deeper(b)) or (inV1(b) and b != 0 and deeper(a))
    # careful: inV1(a) with a==0 excluded already since others has no 0; a in {1,2,3}
    B = ((a == 1 and deeper(b)) or (b == 1 and deeper(a)))
    S = (a == 2 and b == 2)
    return B or S

surv = []
for rest in itertools.product([1, 2, 3], repeat=6):
    w = (0,) + rest
    wins = [(w[i], w[(i+1)%7], w[(i+2)%7]) for i in range(7)]
    # at least one star window: window containing x0 with other two both W
    has_star = any((0 in win and sum(1 for s in win if s == 2) == 2 and win.count(0) == 1) for win in wins)
    if not has_star: continue
    if all(edge(*win) for win in wins):
        surv.append(w)
print("surviving words (x0 fixed at pos0, states X0/A/W/D):", len(surv))
for w in surv[:30]:
    print("  ", w)
