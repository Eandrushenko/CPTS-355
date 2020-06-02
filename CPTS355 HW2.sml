fun palindrome s =
    let val i = ref 0
        val j = ref (String.size s - 1)
        val result = ref true
    in while !i < !j do
           (if String.sub (s, !i) = String.sub (s, !j)
            then (i := !i + 1 ; j := !j - 1)
            else (i := !j ; result := false))
     ; !result
    end
(*https://stackoverflow.com/questions/37122214/standard-ml-palindrome-without-reversing-the-list*)



fun zip L M = 
let
	fun revAppend ([],L) = L | revAppend(x::rest,L) = revAppend(rest,x::L)
	fun reverse L = revAppend(L,[])
	fun zipaux [] [] acc = acc
	| zipaux (x::rest) [] acc = acc
	| zipaux [] (y::rest2) acc = acc
	| zipaux (x::rest) (y::rest2) acc = zipaux rest rest2 ((x,y)::acc);
in
	reverse(zipaux L M [])
end;

(*fun count x [] acc = acc
| count x (y::rest) acc =
if (x=y) 
then count x rest (acc+1)
else count x rest acc;*)

fun areAllUnique [] = true
| areAllUnique [x] = true
| areAllUnique (x::y::rest) = 
if (x = y)
then false
else areAllUnique (x::rest);



(*fun subsets ([]) = [[]]
| subsets (x::rest) =
let	
	fun union ([], rest) = rest
	| union (x::rest,rest2) =
	if member(x, rest)
	then union (rest, rest2)
	else x::union*)

	
fun palindromeTest () =
let
val palT1 = (palindrome  "Madam,I’m Adam" = true)
val palT2 = (palindrome  "Yreka Bakery" = true)
val palT3 = (palindrome  "Doc, note, I dissent, a fast never prevents a fatness.  I diet on cod" = true )
val palT4 = (palindrome  "01/02/2010" = true)
val palT5 = (palindrome  "1/02/2010" = false)
val palT6 = (palindrome  "why am i doing the graders job" = false)
val palT7 = (palindrome  "racecar" = true)
in
print("palindrome:-----------------------------------------------------\ntest1: " ^ Bool.toString(palT1) ^
"   test2: " ^ Bool.toString(palT2) ^
"   test3: " ^ Bool.toString(palT3) ^
"   test4: " ^ Bool.toString(palT4) ^
"   test5: " ^ Bool.toString(palT5) ^
"   test6: " ^ Bool.toString(palT6) ^
"   test7: " ^ Bool.toString(palT7) ^ "\n\n")
end
val _ = palindromeTest()


fun zipTest () =  
let       
val zipT1 = ((zip [1,2,3,4,5] ["one","two"]) = [(1,"one"),(2,"two")])      
val zipT2 = ((zip [1] [1,2,3,4]) = [(1,1)])      
val zipT3 = ((zip [1,2,3,4,5] []) = [])      
val zipT4 = ((zip [] [1,2,3,4,5]) = [])  
val zipT5 = ((zip ["one","two"] [1,2,3,4,5]) = [("one",1),("two",2)])
val zipT6 = ((zip [1,2,3,4] [1]) = [(1,1)])
val zipT7 = ((zip [1,2,3,4,5] [5,4,3,2,1]) = [(1,5),(2,4),(3,3),(4,2),(5,1)])
in       
print ("zip:---------------------------------------------------- \ntest1: " ^ Bool.toString(zipT1) ^              
"   test2: " ^ Bool.toString(zipT2) ^              
"   test3: " ^ Bool.toString(zipT3) ^                
"   test4: " ^ Bool.toString(zipT4) ^
"   test5: " ^ Bool.toString(zipT5) ^
"   test6: " ^ Bool.toString(zipT6) ^
"   test7: " ^ Bool.toString(zipT7) ^ "\n\n")   
end
val _ = zipTest()

fun uniqueTest () =
let
val uT1 = (areAllUnique [1,3,4,2,5,0,10] = true)
val uT2 = (areAllUnique [[1,2],[3],[4,5],[]] = true)
val uT3 = (areAllUnique [(1,"one"),(2,"two"),(1,"one")] = false)
val uT4 = (areAllUnique [] = true)
val uT5 = (areAllUnique [1,2,3,4,1,7] = false)
val uT6 = (areAllUnique [1,1,1,1,1] = false)
val uT7 = (areAllUnique [1,5,8,7,4,6,3] = true)
in
print ("areAllUnique:----------------------------------------- \ntest1: " ^ Bool.toString(uT1) ^
"    test2: " ^ Bool.toString(uT2) ^
"    test3: " ^ Bool.toString(uT3) ^
"    test4: " ^ Bool.toString(uT4) ^
"    test5: " ^ Bool.toString(uT5) ^
"    test6: " ^ Bool.toString(uT6) ^
"    test7: " ^ Bool.toString(uT7) ^ "\n\n")
end
val _ = uniqueTest()







