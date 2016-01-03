# make for px86

main: main.c 
	gcc -m32 -Wall -o px86 main.c instruction.c modrm.c emulator_function.c io.c

test: test.c
	gcc -nostdlib -fno-asynchronous-unwind-tables -g -fno-stack-protector -m32 -c test.c
	nasm -f elf crt0.asm
	ld -m elf_i386 --entry=start --oformat=binary -Ttext 0x7c00 -o test.bin crt0.o test.o

clean: clean
	rm -f *.o px86 test.bin a.out
