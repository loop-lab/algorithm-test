package main

import "fmt"

func getSym(arr [][]int) bool {
	if len(arr) == 1 {
		return true
	}
	if len(arr) == 0 {
		return false
	}

	left := arr[0][0]
	right := arr[0][0]
	left_y := arr[0][1]
	right_y :=arr[0][1]
	arr_map := make(map [int][]int)

	for i := 0; i < len(arr); i++ {
		arr_map[arr[i][1]] = append(arr_map[arr[i][1]], arr[i][0])

		if arr[i] < left {
			left := arr[i][0]
			left_y := arr[i][1]
		}

		if arr[i] > right {
			right := arr[i][0]
			right_y := arr[i][1]
		}
	}

	if left_y != right_y {
		return false
	}

	middle := float32(right + left) / 2

	for y, val := range arr_map {
		sum_x := sum()

		if float32(sum_x) / float32(len(val)) != middle {
			return false
		}
	}

	return true
}

func Test(t *testing.T) {
	fmt.Printf("%+v\n", getSym([[0, 0], [5, 0], (3, 0), (1, 1), (4, 1)]))
	fmt.Printf("%+v\n", getSym([[0, 0), (5, 0), (2.5, 0), (1, 1), (4, 1)]))
	fmt.Printf("%+v\n", getSym([[0, 0), (5, 0), (2.5, 0), (1, 1), (5, 1)]))
	fmt.Printf("%+v\n", getSym([[3, 0]))
	fmt.Printf("%+v\n", getSym([]))
}
