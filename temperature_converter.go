package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Print("ERROR")
		return
	}

	value, err := strconv.ParseFloat(os.Args[1], 64)
	if err != nil {
		fmt.Print("ERROR")
		return
	}

	mode := os.Args[2]

	if mode == "C2F" {
		result := (value * 9 / 5) + 32
		fmt.Printf("%.2f", result)
	} else if mode == "F2C" {
		result := (value - 32) * 5 / 9
		fmt.Printf("%.2f", result)
	} else {
		fmt.Print("ERROR")
	}
}
