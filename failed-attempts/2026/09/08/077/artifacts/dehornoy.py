"""Dehornoy handle reduction for braid words with inverses (n<=4)."""
import sys
sys.path.insert(0, 'artifacts')

def free_reduce(w):
    st = []
    for g in w:
        if st and st[-1] == -g: st.pop()
        else: st.append(g)
    return st

def handle_reduce(w, max_steps=5000):
    """w: list of nonzero ints, k means sigma_{k-1}, -k sigma^{-1}. One pass handle reduction.
    Returns reduced word. A sigma_{m}-handle is pattern (m+1, w_inner, -(m+1)) with no +- (m+1) inside
    and no generator with index > m+1... standard: reduce by replacing with (w_inner with index-m shifted?) 
    We implement: find leftmost handle: positions a<b with w[a]=m+1, w[b]=-(m+1), m = min index-1 in (a..b)? Simplify: use standard rule:
    handle sigma_i ... sigma_i^{-1} with interior using only generators j>i: replace each sigma_j (j>i) by prescribed word.
    Full rule complex; bounded version: eliminate handles of the form s_i e s_i^{-1} where interior has no s_i^{+-1}:
      new interior: for each generator x in interior: if x == i+1... use braid relations expansion.
    For our comparison words (short, n<=4), implement generic: repeatedly apply:
      - free reduction
      - braid relations as rewriting (s_i s_{i+1} s_i -> s_{i+1} s_i s_{i+1}; commutations)
      - handle step for minimal pattern.
    """
    w = free_reduce(list(w))
    for _ in range(max_steps):
        red = free_reduce(w)
        if len(red) < len(w):
            w = red; continue
        # find handle: smallest i>=1 such that exists a<b, w[a]=i, w[b]=-i, no +-i strictly inside, and all interior gens have abs > i... (Dehornoy handle: interior gens index > i only... actually >= ? interior must avoid +-i and use only j>i? No: handle allows interior with indices > i? The rule: sigma_i-handle = w0 sigma_i^{+-} ... with interior free of sigma_i and of higher? )
        found = None
        for a in range(len(w)):
            i = abs(w[a])
            if w[a] != i: continue  # left end must be positive? general handles either sign; take +i start
            for b in range(a+1, len(w)):
                if w[b] == -i:
                    interior = w[a+1:b]
                    if all(abs(x) != i for x in interior) and all(abs(x) > i for x in interior):
                        found = (a, b, i, interior); break
            if found: break
        if not found:
            # try negative-start handles (-i ... +i)
            for a in range(len(w)):
                i = abs(w[a])
                if w[a] != -i: continue
                for b in range(a+1, len(w)):
                    if w[b] == i:
                        interior = w[a+1:b]
                        if all(abs(x) != i for x in interior) and all(abs(x) > i for x in interior):
                            found = (a, b, -i, interior); break
                if found: break
        if not found:
            return w
        a, b, s, interior = found
        i = abs(s)
        # reduction of handle s_i v s_i^{-1} (s=+i): replace by v' where each generator x in v with |x|>i maps:
        # standard handle reduction: sigma_i ... sigma_i^{-1}: delete ends, transform interior: x -> ... for j>i: sigma_j -> sigma_{j} ... (expansion). For j >= i+2 (commuting): unchanged. For j=i+1: sigma_{i+1} -> sigma_{i+1} sigma_i sigma_{i+1}^{-1}?? that reintroduces i. The correct Dehornoy rule: replace each sigma_{i+1}^{e} by sigma_{i+1} sigma_i^{e} ... hmm signs.
        # Use documented rule (Dehornoy, Braids and Self-Distributivity, Prop: handle reduction): if w = s_i^e v s_i^{-e} handle with v using only j>i: then w -> v' where v' obtained from v replacing every s_j^{+-1} (j>i) by: s_j unchanged if j>i+1; s_{i+1}^e' -> s_{i+1} s_i ... Let me use: s_{i+1} -> s_{i+1} s_i s_{i+1}^{-1} s_i^{-1}?? risky.
        # PRAGMATIC: only need sign determination for our witness pair; fall back to brute-force Dehornoy via known faithful action? Instead implement short-word decision via Burckel normal form comparison using our Garside? Simplest rigorous: compare A vs B by checking whether A^{-1}B is Dehornoy-positive via exhaustive search: enumerate all positive words u equivalent to A^{-1}B? Use braid word problem via our perm+Garside? But inverses present.
        return w  # placeholder: no transform applied
    return w
