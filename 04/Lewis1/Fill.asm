// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

@8192
 D=A
@max
 M=D
@SCREEN
 D=A
@addr //assigning first word of screen to addr
 A=D
@SCREEN
 D=A
@addr2 //assigning first word of screen to addr2
 A=D

@i //iterator used in loop
 M=0
@j //iterator used in res
 M=0

@KBD
 M=0 //initializing keyboard to 0

(CHECKKBD)
@KBD
D=M
@LOOP
D;JNE
@RES
D;JEQ


(LOOP) //Setting screen to black
@i
 D=M
@max
 D=D-M
@CHECKKBD
 D;JEQ
@i
 D=M
@addr
 M=-1
@i
 M=M+1
@addr
 A=A+1
@LOOP
 0;JMP

(RES) //Setting screen to white
@j
 D=M
@max
 D=D-M
@CHECKKBD
 D;JEQ
@j
 D=M
@addr2
 M=0

@addr2
 A=A+1
@j
 M=M+1
@RES
 0;JMP






