# Independent mathematical audit

## correctness

PASS

For the stated open neighborhoods in the incidence graph of a finite simple graph, nonempty edge-center traces live only in A and count e_A+lambda_A. The original-vertex centers give nonempty stars on B; if two distinct vertices have the same nonempty star, every edge in it must join those vertices, so simplicity makes them the two endpoints of an isolated marked K2. Subtract one duplicate per such component from |V(H_B)| and use the component Euler formula to get b+p_B-beta_B. The two supports are disjoint except for the separately counted empty trace. All upper-bound deficits are nonnegative; the clique with a helper and separate marked forest saturates them. Adding unmarked edges joining components preserves the saturated terms and a helper outside the marked-edge endpoints witnesses the empty trace, including the single-sort cases. In an extremal marked forest, the components with at least two edges consume all b edges in pairs except for at most one excess edge. The excess is itself a K2 or is absorbed in a three-edge tree, necessarily a claw or P4. Counting vertices gives the claimed minima. Pairing named edge labels gives the even census; in the odd minimum, choose the triple and its claw or one of three middle edges of P4, and pair the rest. Finally for m=a+b the pure A maximum dominates since b(2m-b+1)/2 >= 3b/2 for m>=2; for m=1 check both splits directly. The K2-marked-original construction shatters a pair, while no triple has eight traces. Inspected the supplied checker and recorded output, not executed. It makes 40,000 random draws, skipping empty markings, rather than checking 40,000 nonempty random cases; the reported combined 50,260 checks and the infinite proof do not rely on that wording.

## originality

FAIL

The strongest distinct catalogue record has a different main observable (external-edge traces in a line graph), but its proof explicitly counts the very individual original-vertex signatures needed here and proves their sharp even and odd equality structures, including P4. Substituting this intermediate result and adding the elementary contributions of the other marked sort mechanically gives the law and its equality cases. This is coverage evidence, not a claim about which same-day record appeared first.

## value

FAIL

Distinguishing the two types of marked vertices is natural and the formula is usable, but after crediting the existing exact star count and its rigidity, the surviving material only adds separate trace counts and relabels the already classified small components. Neither the elementary label count nor the standard untyped quadratic bound adds a distinct nonmechanical invariant at this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
