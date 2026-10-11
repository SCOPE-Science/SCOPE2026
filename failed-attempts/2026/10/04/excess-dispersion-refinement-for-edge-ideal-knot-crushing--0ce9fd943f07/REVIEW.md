# Independent mathematical audit

## correctness

PASS

He--Sedgwick--Spreer state that every nontrivial decomposition crush increases the number of ideal edges by exactly two, so after \(m-1\) such crushes the exact total is \(L+2(m-1)\), hence excess over one edge per prime component is \(L+m-2\). Their Lemma 25 construction applies to any nontrivial prime output whose ideal loop has length greater than one. Since the prime outputs are disconnected components, performing one such crush in one component leaves the others available, giving exactly the asserted count of at least \(r\) further crushes. The \(H\)-bound is the correct pigeonhole inequality. Independent symbolic bookkeeping reproduced all identities and the stated \(L=1\), \(d_i\le2\) specialization.

## originality

FAIL

The source proof of Proposition 26 already contains both mechanisms verbatim: each of the \(m-1\) decomposition crushes adds two ideal edges, and any overlength prime output admits the Lemma 25 prime-preserving crush. It even frames a stronger bound in terms of continuing to crush excess ideal edges more controllably. Counting one independently available Lemma 25 crush in every disconnected overlength output is a direct iteration of those stated source lemmas, and \(r\ge\lceil(L+m-2)/H\rceil\) is elementary pigeonhole bookkeeping. Thus the refinement is implication-level covered by the source proof even though it is not written with the variable \(r\).

## value

FAIL

A stronger knot-complexity bound is well motivated, but this record does not establish uniform dispersion or a new crushing mechanism. Its extra term merely counts how many already-separated outputs meet the hypothesis of the source's existing prime-preserving crush, and the \(H\) estimate is elementary. Without a new bound on \(r\) or \(H\), it does not resolve the source's controlled-crushing or tightness question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
