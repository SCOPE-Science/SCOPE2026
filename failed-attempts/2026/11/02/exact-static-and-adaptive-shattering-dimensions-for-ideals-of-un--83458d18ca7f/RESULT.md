# Exact static and adaptive shattering dimensions for ideals of uniform weak orders

## Finding
For integers \(r,h\ge1\), put \(P_{r,h}=A_1\oplus\cdots\oplus A_h\), where \(A_i\) is an antichain of \(r\) elements and every element of \(A_i\) lies below every element of \(A_j\) when \(i<j\). Let \(\mathcal I(P_{r,h})\) be the class of all order ideals, viewed as binary membership functions on the vertices. Then
\[
\operatorname{VCdim}(\mathcal I(P_{r,h}))=r,\qquad
\operatorname{Ldim}(\mathcal I(P_{r,h}))=r-1+\lfloor\log_2(h+1)\rfloor.
\]
Thus their difference is exactly \(\lfloor\log_2(h+1)\rfloor-1\). In particular the adaptive dimension is unbounded at fixed positive width \(r\), despite the static dimension being exactly \(r\). The first strict gap occurs at three levels for every \(r\), and the gap reaches at least \(k\) precisely when \(h\ge 2^{k+1}-1\).

## Assumptions and scope
All posets are finite; the order is reflexive in the usual sense. An order ideal is a down-closed subset. The membership class includes the empty and full ideal. The VC dimension is the maximum cardinality of a coordinate set admitting every binary restriction. The Littlestone dimension is the largest depth of a complete adaptive binary query tree in which every answer branch is realized by some ideal. Values of \(r,h\) are arbitrary positive integers; in the auxiliary lemma \(t\) may be zero and zero-sized endpoint levels are omitted.

## Proof
**The static dimension.** All \(r\) vertices of a single level are shattered: every subset of that level extends to an ideal by including all earlier levels. If a shattered set contained a comparable pair \(x<y\), the pattern \(x=0,y=1\) could not be realized by a downset. Every shattered set is therefore an antichain, of size at most \(r\).

**Restriction recursion.** Let \(L(P)\) be the Littlestone dimension of the ideal concept class of a finite poset \(P\). For every queried point \(x\), conditioning on \(x=0\) eliminates the principal filter \(\uparrow x\); conditioning on \(x=1\) forces the principal ideal \(\downarrow x\). The two nonempty version spaces are isomorphic to the ideals of the induced posets \(P\setminus\uparrow x\) and \(P\setminus\downarrow x\). Consequently, if \(P\) is nonempty,
\[
L(P)=1+\max_{x\in P}\min\{L(P\setminus\uparrow x),L(P\setminus\downarrow x)\},\quad L(\varnothing)=0.
\]
The equality follows immediately by taking the optimal root of a complete binary shattered query tree.

**Sharpened upper lemma.** Fix \(r\ge1\). Consider the weak order \(Q(a,t,b)\) with an initial antichain of size \(a\), then \(t\) levels of size \(r\), then a final antichain of size \(b\), where \(0\le a,b<r\), and omit empty endpoints. We claim
\[
L(Q(a,t,b))\le r-1+\lfloor\log_2(t+1)\rfloor. \tag{1}
\]
Induct on the total number of elements. With \(t=0\), any query in the first nonempty endpoint has a zero branch leaving only an antichain of size at most \(a-1\); any query in the last nonempty endpoint has a one branch leaving only an antichain of size at most \(b-1\). Thus (1) holds (and the empty poset has dimension zero). More generally, a query in an incomplete endpoint has a branch of dimension at most \(r-2\), so its root contribution is at most \(r-1\). For a query in the \(i\)-th complete level, where \(1\le i\le t\), its zero branch corresponds to \(Q(a,i-1,r-1)\), while its one branch corresponds to \(Q(r-1,t-i,b)\). By induction their ranks are at most
\[
r-1+\lfloor\log_2 i\rfloor\quad\text{and}\quad r-1+\lfloor\log_2(t-i+1)\rfloor.
\]
Set \(k=\lfloor\log_2(t+1)\rfloor\). If \(t\ge1\), then \(k\ge1\) and \(i+(t-i+1)=t+1<2^{k+1}\). Hence at least one of \(i,t-i+1\) is strictly below \(2^k\), and the corresponding child rank is at most \(r+k-2\). Adding the root contributes at most \(r+k-1\), proving (1). The argument covers \(r=1\) because both endpoint sizes must then be zero.

Taking \(a=b=0\) and \(t=h\) in (1) gives the desired upper bound \(L(P_{r,h})\le r-1+\lfloor\log_2(h+1)\rfloor\).

**Matching adaptive lower bound.** Select one distinguished point \(e_i\in A_i\) at every level. Their membership vectors as the ideal varies form exactly the \(h+1\) threshold strings consisting of \(j\) leading ones and \(h-j\) trailing zeros, for \(0\le j\le h\). These strings shatter a complete adaptive binary-search tree of depth \(k=\lfloor\log_2(h+1)\rfloor\): recursively query a distinguished level that separates the surviving threshold indices into two sets of at least \(2^{k-1}\) indices. At each depth-\(k\) leaf, choose any compatible threshold index \(j\). There is a subcube of ideals of dimension \(r-1\) realizing that distinguished-string pattern: if \(j=0\), freely choose the nondistinguished vertices in \(A_1\) while setting \(e_1=0\); if \(j\ge1\), freely choose the nondistinguished vertices in \(A_j\) while setting \(e_j=1\); in both cases take earlier levels full and later levels empty. No nondistinguished vertex has been queried on the initial tree. Append the \(r-1\) free coordinate queries at each leaf. Every binary branch is realizable, so \(L(P_{r,h})\ge k+r-1\), finishing the proof.

## Verification
The companion standard-library Python program `verify.py` independently computes Littlestone rank by direct enumeration of ideals and by the exact order-ideal deletion recurrence. It verifies the formula on 18 direct cases with at most 11 vertices, 158 uniform-profile cases through six vertices per level and 21 levels, and 1,183 endpoint-truncation profiles. Direct cases also check \(\operatorname{VCdim}=r\) and \(|\mathcal I(P_{r,h})|=1+h(2^r-1)\). The program reports `UNIFORM_WEAK_ORDER_IDEAL_CHECKS_PASS 18 158 1183 186` when all assertions succeed. These finite checks supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work
Alon, Livni, Malliaris and Moran (2018) study Littlestone dimension and threshold patterns at the general concept-class level, including the online complexity of threshold classes; this motivates the distinguished-coordinate search but does not state the two-parameter weak-order ideal formula in the inspected HTML text. Alon, Beimel, Moran and Stemmer (2020, §4.1) prove general Littlestone bounds for unions of concept classes; their published propositions do not address this order-ideal class. The paper of Campo and Erné (2019) counts downsets of finite posets, which is distinct from the adaptive shattering rank. Its abstract was checked, but its full PDF was not successfully retrieved; no whole-paper noncoverage claim is made. The proof here uses an explicit restriction recurrence and the endpoint-truncation invariant, rather than assuming an invalid additive union bound. A search of published mathematical records and available previous work did not establish equivalent coverage; historical priority is not certified.

## Limitations
This is an exact theorem for uniform weak orders, not for all posets or arbitrary nonuniform level sizes. The finite verifier does not independently certify the infinite argument. A fully exhaustive historical-priority survey and an independent external review have not been performed. The earlier downset-counting article is not fully inspected; it remains an access-related priority risk.

## References
- N. Alon, R. Livni, M. Malliaris, S. Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949v1, first submitted 2018-06-04. https://arxiv.org/abs/1806.00949
- N. Alon, A. Beimel, S. Moran, U. Stemmer, *Closure Properties for Private Classification and Online Prediction*, manuscript dated 2020-05-12, §4.1. https://web.math.princeton.edu/~nalon/PDFS/Closure2.pdf
- F. a Campo and M. Erné, *Exponential functions of finite posets and the number of extensions with a fixed set of minimal points*, J. Combin. Math. Combin. Comput. 110 (2019), 125–156, publisher metadata dated 2019-09-30. https://combinatorialpress.com/jcmcc-articles/volume-110/exponential-functions-of-finite-posets-and-the-number-of-extensions-with-a-fixed-set-of-minimal-points/
