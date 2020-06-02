
fun exists (y, []) = false
 |  exists (y, x::rest) = 
if (y=x) 
then true
else exists(y, rest);

(*A plain type variable like 'a can be substituted with an arbitrary type. 
The form ''a is a so-called equality type variable, 
which means that it can only be substituted by types that 
admit the use of the equality operator = (or <>) on their values.
https://stackoverflow.com/questions/20437520/what-is-the-difference-between-a-and-a-in-sml

This basically means that 'a is arbitrary but ''a is arbibtary and an operator will be used on it*)

fun myTest_exists(y, L, output) = if (exists (y, L)) = output then true else false;

fun listUnion([], y) = y
|   listUnion(a::x, y) =
if exists(a,y) 
then listUnion(x, y)
else a::listUnion(x, y);

fun myTest_union(L, y, output) = if (listUnion (L, y)) = output then true else false;

fun listIntersect([], y) = []
|   listIntersect(a::x, y) =
if exists(a, y) 
then a::listIntersect(x, y)
else listIntersect(x, y);


fun myTest_intersect(L, y, output) = if (listIntersect (L, y)) = output then true else false;

fun nthElement [] x = "N/A"
| nthElement (y::rest) 1 = y
| nthElement(y::rest) x = 
if (x <= length(y::rest))
then (nthElement rest (x-1))
else "N/A";

fun myTest_element(L, y, output) = if (nthElement L y) = output then true else false;


fun isSorted [] = true
| isSorted [y] = true
| isSorted (x::y::rest) =
if (x <= y)
then isSorted(y::rest)
else false;

fun myTest_sorted(L, output) = if (isSorted L) = output then true else false;

fun reverse nil = nil | reverse (x::xs) = (reverse xs) @ [x];
(*obtained from http://cs.fit.edu/~ryan/sml/programs/lists-sml.html*)

fun aux n [] buffer = [buffer]
| aux n (x::rest) buffer =
if (length(buffer) < n)
then (aux n rest (x::buffer))
else (buffer::(aux n rest(x::[])));

fun attempt L = map reverse L;

fun pairNright n L = attempt(aux n L []);

fun myTest_pairNright (n, L, output) = if (pairNright n L) = output then true else false;

(*pairNLeft was not attempted so + 12.5 percent rather than the full 25?*)

val exists_test1 = myTest_exists(2, [1, 2, 3, 4], true);
val exists_test2 = myTest_exists(3, [1, 2, 5, 4, 8, 7], false);
val exists_test3 = myTest_exists(4, [], false);

val listUnion_test1 = myTest_union([1,2,3], [], [1,2,3]);
val listUnion_test2 = myTest_union([1,2,3], [2,3,4], [1,2,3,4]);
val listUnion_test3 = myTest_union([], [2,3,4], [2,3,4]);

val listIntersect_test1 = myTest_intersect([1,2,3], [2,3,4], [2,3]);
val listIntersect_test2 = myTest_intersect([], [2,3,4], []);
val listIntersect_test3 = myTest_intersect([1,2,3], [1,1,2], [1,2]);

val nthElement_test1 = myTest_element([], 4, "N/A");
val nthElement_test2 = myTest_element(["A","B","C", "D"], 3, "C");
val nthElement_test3 = myTest_element(["E","F","G","H","I"], 1, "E");

val isSorted_test1 = myTest_sorted([1,2,3], true);
val isSorted_test2 = myTest_sorted([1,4,3,5,8], false);
val isSorted_test3 = myTest_sorted([1,1,2,2,3], true);

val pairNright_test1 = myTest_pairNright(2, [1,2,3,4,5], [[1,2],[3,4],[5]]);
val pairNright_test2 = myTest_pairNright(3, [1,2,3,4,5], [[1,2,3],[4,5]]);
val pairNright_test3 = myTest_pairNright(4, [1,2,3,4,5], [[1,2,3,4],[5]]);










