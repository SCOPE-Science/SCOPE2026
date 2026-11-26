# Independent mathematical audit

## correctness

PASS

Put m=n−1 and label a word supported on i<j by (a,b)=(i,j−1). Its weight-one descendants have labels a,b, coinciding only for a loop. With t loops and e other words, disjointness gives t+2e≤m. Consecutive loops collide in the adjacent weight-two output, so t≤ceil(m/2), giving the upper bound including n=2. The odd loops and even pairs (4k+2,4k+4) attain it: their weight-one labels are disjoint; weight-two loop outputs have gap 1, while selected nonloops have gaps 2 or 3 and disjoint first-coordinate sets for different k. The code with n=2 is {11}. An independent finite check enumerated all weight-two words, deleted each of the n positions and deduplicated the results, then exactly maximized a clique in the graph with adjacency defined by disjoint deletion sets. The maxima for n=2 through 10 were 1,1,2,3,4,4,5,6,7. This is corroboration; the packing and construction prove the unbounded claim. The supplied script was inspected as text, not run.

## originality

FAIL

Distinct available Resultary records already state this same theorem for all n≥2. The strongest inspected match also gives the same upper-bound argument and the same construction. This is demonstrable equivalent coverage, not an inference about priority or provenance from catalog dates.

## value

FAIL

A first exact optimum and explicit witnesses for this natural layer would be useful, but the submitted result supplies the same bound, packing argument and witnesses as the distinct exact records. It does not isolate an additional invariant or improvement that would justify the duplicate as a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
