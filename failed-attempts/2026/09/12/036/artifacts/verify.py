"""Independent verifier for lane-1131 TARGET claim (stdlib only).

Checks the explicit block list in witness_blocks.json:
  (V1) 48 distinct triples on point set {0..18}.
  (V2) Pair-disjointness: 144 distinct covered pairs (partial STS).
  (V3) Pasch-freedom: 0 Pasches (brute-force census over all C(48,4) quads;
       Pasch := 4 blocks on exactly 6 points, every point of degree 2).
  (V4) Leave graph: exactly 27 edges, triangle-free (brute-force census).
Corollaries (pure logic, no SAT needed):
  (C1) Linear-maximality: a triple addable without repeating a pair would be
       a triangle in the leave; there are none, so no triple can be added.
  (C2) Non-completability: any STS(19) containing P would add exactly 9 blocks
       partitioning the 27 leave pairs, each a leave triangle. Contradiction.
Usage: python3 verify.py  (run from output/artifacts/)
"""
import itertools, json, collections, sys, os

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "witness_blocks.json")) as f:
        data = json.load(f)
    F = [tuple(B) for B in data["blocks"]]
    pts = set(range(19))

    # V1
    assert len(F) == 48, f"need 48 blocks, got {len(F)}"
    assert len(set(F)) == 48, "blocks not distinct"
    for B in F:
        assert len(B) == 3 and set(B) <= pts and len(set(B)) == 3, f"bad block {B}"
        assert list(B) == sorted(B), f"block not normalized {B}"
    assert pts == {p for B in F for p in B}, "point set is not all of [19]"
    print("V1 OK: 48 distinct normalized triples covering all of [19]")

    # V2
    pairs = [(a, b) for (a, b, c) in F for (a, b) in ((a, b), (a, c), (b, c))]
    assert len(set(pairs)) == 144 == 3 * 48, "pair overlap or miscount"
    print("V2 OK: 144 distinct covered pairs (partial Steiner triple system)")

    # V3
    npasch = 0
    for quad in itertools.combinations(F, 4):
        u = set().union(*[set(B) for B in quad])
        if len(u) != 6:
            continue
        deg = collections.Counter(p for B in quad for p in B)
        if all(deg[p] == 2 for p in u):
            npasch += 1
    assert npasch == 0, f"found {npasch} Pasches"
    print("V3 OK: Pasch census over C(48,4)=194580 quads gives 0 Pasches")

    # V4
    used = set(pairs)
    leave = [(i, j) for i in range(19) for j in range(i + 1, 19)
             if (i, j) not in used]
    assert len(leave) == 27 == 19 * 18 // 2 - 144, f"leave has {len(leave)} edges"
    adj = {p: set() for p in range(19)}
    for (i, j) in leave:
        adj[i].add(j)
        adj[j].add(i)
    ntris = sum(1 for i in range(19) for j in adj[i] if j > i
                for k in adj[i] & adj[j] if k > j)
    assert ntris == 0, f"leave has {ntris} triangles"
    print("V4 OK: leave graph has exactly 27 edges and 0 triangles")

    print("C1 OK: triangle-free leave => no triple addable without pair repeat "
          "(linear-maximal)")
    print("C2 OK: 57-48=9 missing blocks would partition 27 leave pairs into "
          "triangles => no STS(19) extends P (non-completable)")
    print("VERIFY_OK")

if __name__ == "__main__":
    sys.exit(main())
