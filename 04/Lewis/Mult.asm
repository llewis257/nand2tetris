// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@1
 D=M 
@m
 M=D // n=RAM[1]

@0
 D=M 
@n
 M=D // m=RAM[0]

@i
 M=0 //i=0
@2
 M=0 //Initialize R2 to zero

//if any of the number is zero
	@n
	 D=M
	@LOOP0
	 D;JEQ
	
	@m
	 D=M
	@LOOP0
	 D;JEQ 
	

//is m greater than n?
	@n
	 D=M
	@m
	 D=D-M

	@LOOP2
	 D;JLT


(LOOP1) //if n=RAM[0] is greater than m we make: n+...+n (m times)
	@m
	 D=M
	@i
	 D=D-M
	@END
	 D;JEQ
//Addition starts here
	@n
	 D=M
	@2
	 M=M+D
	@i // i++
	 M=M+1
	@LOOP1
	 0;JMP
(LOOP2) //if m=RAM[1] is greater than n we make: m+...+m (n times)
	@n
	 D=M
	@i
	 D=D-M
	@END
	 D;JEQ
//Addition starts here
	@m
	 D=M
	@2
	 M=M+D
	@i // i++
	 M=M+1
	@LOOP2
	 0;JMP
(LOOP0) 
 	@2
	 M=0

(END)
	@END
 	 0;JMP





