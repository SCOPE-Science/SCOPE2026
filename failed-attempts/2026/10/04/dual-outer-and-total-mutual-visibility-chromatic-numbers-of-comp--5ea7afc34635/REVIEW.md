# Independent mathematical audit

## correctness

PASS

The displayed chromatic-number formulas themselves are correct. I independently brute-forced all 111 dual/outer/total cases for complete-multipartite profiles through order seven with no mismatch. The universal proof follows from the same-part criterion: two vertices in one part are \(M\)-visible exactly when the complement of \(M\) contains a vertex in a different part. However, the submitted RESULT contains a genuine proof error in its total-coloring paragraph for \(r\ge3\): the proposed partition \(V_1, V\setminus V_1\) is not always total (for example, in \(K_{2,1,1}\), the class \(V\setminus V_1\) blocks every geodesic between the two vertices of \(V_1\)). A correct two-color proof instead splits two non-singleton parts, or, when only one part is non-singleton, splits it and assigns singleton parts to both colors. Thus the theorem is true even though this record's written proof is defective.

## originality

FAIL

An earlier record in the same repository states the identical three complete-multipartite formulas, with the same star boundaries and a correct family proof. Git history places that `colorings` record at commit `825c27fdbe092bbba0fcce73e9b7a7cf7b698c97` at 2026-10-04T05:55:02Z, while this `chromatic-numbers` record was imported at commit `046f9b2a112f73cf492301471fd438efd9d6577f` at 2026-10-04T05:55:18Z. The later record is therefore exact duplicate coverage, not an independent original result.

## value

FAIL

The complete-multipartite phase diagram is mathematically useful, but this record contributes no independent scientific content because the same theorem had already been imported in the same repository moments earlier. Its written proof also introduces an avoidable incorrect construction. Under the standalone value criterion, a duplicate restatement is not a worthwhile new gap closure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
