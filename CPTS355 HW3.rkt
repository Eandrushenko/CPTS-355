#lang racket


;replace
(define (aux_replace n v L M) (cond
                         [(= (length L) 0) M]
                         [(= n 0) (aux_replace (- n 1) v (cdr L) (cons v M))]
                         [else (aux_replace (- n 1) v (cdr L) (cons (car L) M))]))
(define (replace n v L)
  [reverse(aux_replace n v L null)])

;mergeUnique2
(define (merge L1 L2 M) (cond
                          [(> (length L1) 0) (cond
                                               [(eq? #f (member (car L1) M)) (merge (cdr L1) L2  (cons (car L1) M))]
                                               [else (merge (cdr L1) L2 M)])]
                          [(> (length L2) 0) (cond
                                               [(eq? #f (member (car L2) M)) (merge L1 (cdr L2) (cons (car L2) M))]
                                               [else (merge L1 (cdr L2) M)])]
                          [else M]))

(define (mergeUnique2 L1 L2)
  [sort(merge L1 L2 null) <])

;mergeUniqueN
(define (mergeUniqueN Ln)
  [foldr mergeUnique2 (car Ln) (cdr Ln)]) 

;numberToSum
(define (aux_sum sum L M n) (cond
                            [(>= n sum) M]
                            [else (aux_sum sum (cdr L) (cons (car L) M) (+ (car L) n))]))

(define (numbersToSum sum L)
  [reverse (cdr (aux_sum sum L null 0))])

;flatten
(define (flatten L) (cond
                           [(null? L) null]
                           [(list? (car L)) (append (flatten (car L)) (flatten (cdr L)))]
                           [else (cons (car L) (flatten (cdr L)))]))


;unzip
(define (unzip_aux L) (car L))
(define (unzip_aux2 L) (car (cdr L)))

(define (unzip L)
  [cons (map unzip_aux L) (list (map unzip_aux2 L))])

;Stream of Squares
(define squares
  (letrec (
           [f (lambda (x) (cons x (lambda () (f (* (+ 1 (sqrt x)) (+ 1 (sqrt x)))))))])
    (lambda () (f 1))))

(define (numUntil Stream n)
  (if (<= n (car (Stream)))
      null
      (cons (car (Stream)) (numUntil (cdr (Stream)) n))))


;streamSum
(define (streamSum_aux sum Stream M n) (cond
                                 [(>= n sum) M]
                                 [else (streamSum_aux sum (cdr (Stream)) (cons (car (Stream)) M) (+ (car (Stream)) n))]))

(define (streamSum sum Stream)
  [reverse (cdr (streamSum_aux sum Stream null 0))])

;helper function to print the test result
(define (bool2str val) (if val "true" "false"))

;test functions
(define (testflatten)
  (let* ([T1 (equal? (flatten '(1 (2 (3 4(5 6)7(8(9(10)11)))))) '(1 2 3 4 5 6 7 8 9 10 11) )]
         [T2 (equal? (flatten '((1)(2 (2)) (3(3(3))) (4(4(4(4)))))) '(1 2 2 3 3 3 4 4 4 4) )]
         [T3 (equal? (flatten '( () )) '() )] )
        (display(string-append "\n-------\n flatten \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (testreplace)
  (let* ([T1 (equal? (replace 3  40 '(1 2 3 4 (5) "6")) '(1 2 3 40 (5) "6") )]
         [T2 (equal? (replace 4  5 '(1 2 3 4 (5) "6")) '(1 2 3 4 5 "6") )]
         [T3 (equal? (replace 0  9 '("6" 10 11 12 )) '(9 10 11 12) )] )
                 (display(string-append "\n-------\n replace \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))


(define (testMergeUnique)
  (let* ([T1 (equal? (mergeUnique2 '(4 6 7) '(3 5 7)) '(3 4 5 6 7) )]
         [T2 (equal? (mergeUnique2 '(1 5 7) '(2 5 7)) '(1 2 5 7) )]
         [T3 (equal? (mergeUnique2 '() '(3 5 7)) '(3 5 7) )] )
    (display(string-append "\n-------\n mergeUnique2 \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (testMergeUniqueN)
  (let* ([T1 (equal? (mergeUniqueN '(1)) 1 )]
         [T2 (equal? (mergeUniqueN '((2 4 6) (1 4 5 6))) '(1 2 4 5 6) )]
         [T3 (equal? (mergeUniqueN '((2 4 6 10) (1 3 6) (8 9))) '(1 2 3 4 6 8 9 10) )] )
        (display(string-append "\n-------\n mergeUniqueN \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (testunzip)
  (let* ([T1 (equal? (unzip '((1 2) (3 4) (5 6))) '((1 3 5) (2 4 6)) )]
         [T2 (equal? (unzip '((1 “a”) (5 “b”) (8 “c”))) '((1 5 8) (“a” “b” “c”)) )]
         [T3 (equal? (unzip '(("this" "and") ("is" "it") ("a" "works") ("test" ":)"))) '(("this" "is" "a" "test") ("and" "it" "works" ":)")) )] )
            (display(string-append "\n-------\n unzip \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (testnumbersToSum)
  (let* ([T1 (equal? (numbersToSum 100  '(10 20 30 40)) '(10 20 30) )]
         [T2 (equal? (numbersToSum 30  '(5 4 6 10 4 2 1 5)) '(5 4 6 10 4) )]
         [T3 (equal? (numbersToSum  5  '(5 4 6)) '() )] )
                (display(string-append "\n-------\n numbersToSum \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (testStreamofSquares)
  (let* ([T1 (equal? (numUntil squares 10) '(1 4 9) )]
         [T2 (equal? (numUntil squares 100) '(1 4 9 16 25 36 49 64 81) )]
         [T3 (equal? (numUntil squares 1000) '(1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961) )] )
                    (display(string-append "\n-------\n Stream of Squares \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

(define (teststreamSum)
 (let* ([T1 (equal? (streamSum 10000 squares) '(1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900) )]
        [T2 (equal? (streamSum 200000 squares) '(1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784 841 900 961 1024 1089 1156 1225 1296 1369 1444 1521 1600 1681 1764 1849 1936 2025 2116 2209 2304 2401 2500 2601 2704 2809 2916 3025 3136 3249 3364 3481 3600 3721 3844 3969 4096 4225 4356 4489 4624 4761 4900 5041 5184 5329 5476 5625 5776 5929 6084 6241 6400 6561 6724 6889) )]
        [T3 (equal? (streamSum 100 squares) '(1 4 9 16 25 36) )] )
                       (display(string-append "\n-------\n streamSum \n  T1: " (bool2str T1)
                           ",  T2: " (bool2str T2)
                           ",  T3: " (bool2str T3)))))

;Calling the Test Functions
(testflatten)
(testreplace)
(testMergeUnique)
(testMergeUniqueN)
(testunzip)
(testnumbersToSum)
(testStreamofSquares)
(teststreamSum)
  














