# The first fourth-moment distinction between cyclic and Klein four-colour surjections

## Finding
Let \(H\) be either \(C_4=\mathbb Z/4\mathbb Z\) or \(V_4=(\mathbb Z/2\mathbb Z)^2\). For \(n=4,5,6\), let \(S_{n,H}\subset H^n\) consist of all labelled words that use every element of \(H\), and let \(f_{n,H}=\mathbf1_{S_{n,H}}\). Use the **unnormalized** character transform \(\widehat f_{n,H}(\chi)=\sum_{x\in H^n}f_{n,H}(x)\overline{\chi(x)}\). Its absolute-multiplier histogram \(h_{n,H}(r)=\#\{\chi:|\widehat f_{n,H}(\chi)|=r\}\) is **identical for the two group structures** when \(n=4\) and \(n=5\), but different for the first time at \(n=6\). The complete histograms, with all omitted entries zero, are:

| \(n\) | Group | Nonzero entries \(r:h_{n,H}(r)\) |
|---|---|---|
| 4 | Either | \(0:192,\ 8:60,\ 24:4\) |
| 5 | Either | \(0:828,\ 16:90,\ 32:60,\ 48:45,\ 240:1\) |
| 6 | \(C_4\) | \(0:3072,\ 8:510,\ 24:110,\ 40:192,\ 88:15,\ 104:150,\ 120:1,\ 200:45,\ 1560:1\) |
| 6 | \(V_4\) | \(0:3072,\ 8:540,\ 40:270,\ 88:45,\ 104:120,\ 120:3,\ 200:45,\ 1560:1\) |

In particular, the first separating even Fourier moment is the fourth. At \(n=6\),
\[
\sum_{\chi\in\widehat{C_4^6}}|\widehat f_{6,C_4}(\chi)|^4
-\sum_{\chi\in\widehat{V_4^6}}|\widehat f_{6,V_4}(\chi)|^4
=1{,}132{,}462{,}080.
\]
All second moments coincide by Parseval, including at length six. Equivalently, the ordered additive energies of the two surjection sets at length six differ by exactly \(276{,}480\), with the cyclic value larger. Both length-six convolution operators have rank \(1024\) and smallest positive multiplier \(8\): neither rank nor sharp positive-spectrum condition number detects the group law at this length.

## Assumptions and scope
The underlying *set* of words uses the same four symbols and is independent of which of the two abelian group operations is assigned to them. Symbols are labelled. For \(C_4\), identify symbols with \(0,1,2,3\) and characters with \(\chi_k(x)=i^{kx}\). For \(V_4\), identify symbols with bit pairs and characters with \(\chi_k(x)=(-1)^{k\cdot x}\). Products of these characters give the character groups of \(H^n\). For \(n=4,5,6\), the surjection-set cardinalities are respectively \(24,240,1560\), as obtained by inclusion-exclusion \(4^n-4\cdot3^n+6\cdot2^n-4\).

## Proof
This is a complete finite theorem, proved by the exact-integer exhaustive algorithm `verify_compare.py` included in the package. Its range consists of every \(4^n\) input word, every \(4^n\) character, both group laws, and each of the three claimed lengths; no random samples or incomplete search are used.

First construct \(f_{n,H}\) by enumerating all four-symbol words and setting its entry to one precisely when the four symbols all occur. The same input vector is used for either group. For each coordinate, apply the indicated \(4\times4\) character table. The cyclic table has entries \(i^{ab}\), represented as pairs of *exact integers* for real and imaginary parts, while the Klein table has the four mutually orthogonal Walsh rows \((1,1,1,1)\), \((1,-1,1,-1)\), \((1,1,-1,-1)\), and \((1,-1,-1,1)\). Every transform step is a sum of four Gaussian-integer products, so it is exact and finite. Since the coordinate tables are the exact character tables, iterating through all coordinates computes precisely the full tensor-product transform. The routine then counts every absolute coefficient, producing exactly the four histogram rows displayed in the Finding.

The checker asserts the entire histogram against literal integer dictionaries, not only an aggregate rank or moment. Summing \(r^4h(r)\) gives at length six \(6{,}013{,}593{,}845{,}760\) for the cyclic group and \(6{,}012{,}461{,}383{,}680\) for the Klein group, proving the stated difference. The fourth moments at lengths four and five are respectively \(1{,}572{,}864\) and \(3{,}625{,}451{,}520\) for either group; the full histograms, not merely these moments, agree there. The second moment at length six is \(4^6\cdot1560=6{,}389{,}760\) for each group. Character orthogonality gives \(\sum_\chi|\widehat f(\chi)|^4=|H|^n E(S)\), where \(E(S)=\#\{(a,b,c,d)\in S^4:a+b=c+d\}\), so dividing the fourth-moment difference by \(4^6\) gives the energy difference. Finally the nonzero histogram counts are \(64,196,1024\), and the smallest positive length-six multiplier is eight, as asserted.

## Verification
Execute `python verify_compare.py` using Python's standard library; it reports three `PASS` lines. The independent, differently structured programs `check_klein.py` and `check_cyclic.py`, executable independently with Python, enumerate the same surjections and use separate Walsh and Gaussian-integer butterfly transforms. Each checks its whole frequency support for lengths four through eight and exact Parseval identities; their results agree with the length-four-through-six rank and zero-count consequences of the histograms. The certificate is exhaustive within the finite domain, but does not assert any untested length-sixteen or all-length moment comparison.

## Relationship to prior work
Counting onto words is classical Stirling-number occupancy combinatorics. Bóna–Mező (2007) provide nearby partition-enumeration context, but their partition-root theorems do not specify the two additive group structures or Fourier energy. The published published-finding corpus finding *Exact first-band Fourier sampling spectra on surjective words* (2026) supplies degree-one Gram spectra for general palettes, not the full four-symbol convolution multiplier distribution or this fourth-moment comparison. A separate exact Klein-four surjection Fourier spectrum was already available before the present comparison; the Klein histogram by itself is not claimed as new. What is new here is the **cyclic-versus-Klein comparison**, its first length of divergence and the complete, exactly verified length-six difference. The relationship was tested at the level of statements and implications, not just by comparing titles. No global historical-uniqueness claim is made.

## Limitations
The first-divergence assertion concerns the nonempty surjection sets at lengths four, five and six only. It does not classify the group-law differences for every larger length. The claim is exact but finite; the proof is an exhaustive executable certificate rather than a short symbolic all-length derivation. The bounded literature search cannot exclude an older unindexed comparison, particularly in additive-energy or occupancy literature. No independent mathematical audit has been performed.

## References
- M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734, first public version 2007-05-18, https://arxiv.org/abs/0705.2734 . Background on Stirling partition enumerations, not the Fourier claim.
- *Exact first-band Fourier sampling spectra on surjective words*, published published-finding corpus mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-first-band-fourier-sampling-spectra-on-surjective-words--38dfe55b7163 . A related but non-dominating degree-one result.
