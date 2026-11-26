# Independent mathematical audit

## correctness

PASS

For a proposed fort with original part A and edge-vertex part Q, the exact tests are δ(A)⊆Q and deg_Q(v)≠1 at all v∉A. With A empty, any nonempty eligible Q contains a cycle, and no proper nonempty subset of a cycle has minimum nonzero degree at least two. With A all originals, the original set is itself minimal by the cut test. If both shores of δ(A) have at least two vertices then it contains a 4-cycle; if |A|=1 then the exterior degree test adds a leaf-to-leaf edge to its star, creating a triangle. The remaining case |A|=n−1 gives the stated star fort, which is minimal: cutting any proper nonempty subset of its originals would require an edge inside the leaves, and no subfort without originals fits inside a star. Forcing is equivalent to hitting the minimal forts by the first-entry and terminal-white-set arguments. With nonempty U, the white edge set must be a forest; a singleton U={v} fails the special-fort test exactly when that forest contains the entire star at v, in which case it equals the star. Forest rank n−1−|R| in the Tutte exponent difference gives the displayed identity, and Cayley's formula counts the minimum sets after subtracting one star for each singleton. These arguments include n=3. Independent literal tests exhausted 64, 1024 and 32768 initial sets at n=3,4,5 and matched the exact fort families, forcing sets, and coefficients. Fort totals were 5,12,43; forcing totals 46,566,9016; minimum-set counts 6,60,620. Replay: python3 /workspace/reproductions/check_subdivision.py 3 4 5. The frozen n=6 sample was not independently replayed and is not exhaustive. The bundled script's Python 3.8 compatibility guidance should say 3.10 or later because of int.bit_count(); this does not affect the theorem or independent check.

## originality

FAIL

The companion frozen result and the exact indexed Resultary statement cover the same fort families, all-set test and full labeled enumerator. The specialization of the Tutte polynomial is the same forest sum, not a different invariant. This is demonstrable equivalent coverage, without inferring any publication ordering from directory dates.

## value

FAIL

A full obstruction theorem for a natural subdivision family would be useful in isolation, but the same full labeled answer is already present in the compared results. The Tutte notation mechanically repackages the forest enumerator without a distinct result or new class of graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
