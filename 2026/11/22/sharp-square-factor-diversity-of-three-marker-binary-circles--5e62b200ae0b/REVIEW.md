# Independent mathematical audit

## correctness

PASS

A permitted square has zero or two ones. A mixed square around central gap g has root 0^x1 0^(g−x), with max(0,g−R)≤x≤min(g,L) for its outside gaps L,R. These fits imply length at most n. Unequal central gaps give different words, so only repeated central gaps require taking an interval union. For a=b<c the a-intervals both give offsets 0..a, while the c-interval contributes (2a−c+1)_+; for a<b=c the c-intervals are 0..a and c−a..c, giving min(c+1,2a+2). This verifies the complete piecewise count including ties and zero gaps. For distinct sorted gaps with c≤a+b+1, S=n−3=3a+2x+y, x=b−a, y=c−b, and Q=n−2(x+y)+floor(c/2). The unique smallest x+y in each residue class is attained at (1,1),(1,2),(2,1) respectively. Increasing that sum by h≥1 increases c by at most (2h+1)/3, too little to offset 2h. The repeated-gap bound 5S/6+3 and the c>a+b+1 bound 3S/4+2 are both strictly below the candidate lower bound 7S/6−4 for S≥22. Thus the six permutations give exactly two rotation classes, and the formulas yield the limit 7/6. An independent exhaustive bit scan with one marker anchored confirmed every small maximum, the optimizer permutations at lengths 25–32, and first excess at n=30 with 31 squares; replay with python3 /workspace/audit_checks.py 3. At weight two only the shorter central gap p≤q can be used, giving floor(q/2)+p+1 squares, at most n; weight zero or one allows only all-zero squares.

## originality

PASS

Credit is limited to the sharp optimization at fixed circumference and weight three, full rigidity, and exact first above-circumference length at that weight. The same-day distinct corpus record contains the identical pointwise counting formula and more pointwise structure; that formula is not credited. Its mean, limiting distribution, and ability to evaluate any input do not already determine the exact optimizers without a new extremal argument.

## value

PASS

Three is the first possible marker weight for exceeding the number of positions, a natural sparsity threshold. The theorem gives the first circumference realizing it, the two optimizing rotation classes for all large lengths, and a strict 7/6 versus 1 density separation. This quantifies what is possible with only three marked positions and explains the balanced-but-distinct gap mechanism, beyond a pointwise census or a collection of finite maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
