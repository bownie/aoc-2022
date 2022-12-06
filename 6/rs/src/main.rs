use std::env;
use std::fs;


// From:
//
// https://www.geeksforgeeks.org/rust-array/
fn solve_with_arrays(contents: String) {
    let mut thing:[i32;4] = [-1, -1, -1, -1];
 
    
    let window_size = 4;

    for c in contents.chars() {


        for p in 0..4 {
            if thing[p] == -1 {
                thing[p] = c as i32;
            }
        }


     //   print!("{}",i);
    }
}

/* 
fn solve_with_hashset

fn solve_with_bitset

fn solve_with_slice
itertools

or  

hashset with homogenous tuples
*/



// Show the bit flag concept
//
fn test_print() {
    let mut buf = 0_u32;
    let chars = "abcdef".to_string();

    for c in chars.chars() {
        buf |= 1 << (c as u8 - b'a');
        println!("{} = {}", c, buf)
    }
}
     
fn solution(input: &str, distinct_num: usize) -> Option<usize> {
    for i in 0..input.len() {
        let mut buf = 0_u32;
        let chars = &input[i..i + distinct_num];
        for c in chars.chars() {
            //print!("{}",c);
            buf |= 1 << (c as u8 - b'a');
        }
        if buf.count_ones() == distinct_num as u32 {
            return Some(i + distinct_num);
        }
    }
    None
}

fn main() {

    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");


    let window_size = 14;
    test_print();

    match solution(&contents, window_size) {
        Some(x) => {
            print!("\n");
            println!("Solution for window {} = {}",window_size,x);
        },
        None => {
            print!("No result");
        }

    }
    //solve_with_arrays(contents);

}