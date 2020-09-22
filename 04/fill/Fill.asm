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
 M=D //declaring the loop count

 
(START) //start over when iteration is over
	@index
	 M=0     // when index = 0
(CHECKKBD)
	@KBD
	 D=M
	@RES
	 D;JEQ   // goto RES (Reset screen to white) if KBD value is 0
	@LOOP
	 D;JNE


(LOOP) //Setting screen to black
	@index
        D=M
        @SCREEN
        A=A+D   // Calculate byte address
        M=-1    // Fill with black
        @END
        0;JMP   // goto END

(RES) //Reseting screen
	@index
        D=M
        @SCREEN
        A=A+D   // iterate over screen adresses
        M=0     // 16-bit 0 gives a white pixel

(END)   
        @index
        MD=M+1  // Increment the iteration variable "index"
        @max
        D=D-M
        @START
        D;JEQ   // goto LOOP if max-index is 0
        @CHECKKBD
        0;JMP   // goto check keyboard again





