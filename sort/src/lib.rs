#![warn(missing_docs)]

//! This is sorting crate created for testing purpose 

use std::{marker::PhantomData, mem::swap};

/// wrapper around `std::mem::swap()` 
/// Trait that all sorting algorithm will use 
pub trait Sort{
    /// output type
    type Output;
    /// sorting function
    fn sort(data: &mut Vec<Self::Output>);
}

struct QuickSort<T: PartialEq+PartialOrd> (PhantomData<T>);

impl<T> Sort for QuickSort<T>
where T: PartialEq+PartialOrd
{
    type Output = T;
    fn sort(data: &mut Vec<T>){
        Self::quicksort(data, 0, data.len());
    }
}

impl<T> QuickSort<T>
where T: PartialEq+PartialOrd
{
    fn quicksort(data: &mut Vec<T>, p: usize, r: usize) {
       let q = Self::partition(data,p,r); 
       Self::quicksort(data,p,q);
       Self::quicksort(data,q+1,r);
    }

    fn partition(data: &mut Vec<T>, p:usize, r:usize) -> usize {
        let pivot = r;
        todo!();
    }
}


struct MergeSort<T: PartialEq+PartialOrd+Clone> (PhantomData<T>);

impl<T> MergeSort<T> 
where T: PartialOrd+PartialEq+Clone {
    fn mergesort(data: &mut Vec<T>,p: usize, r: usize) {
        if p > r {
            let q = (p + r)/2;
            Self::mergesort(data,p,q);
            Self::mergesort(data,q+1,r);
            Self::partition(data,p,q,r);
        }
    }

    fn partition(data: &mut Vec<T>, p:usize, q:usize, r:usize) {
        let left_array_size = q - p;
        let right_array_size = r - q + 1;

        let mut left_array: Vec<T> = Vec::with_capacity(left_array_size);
        let mut right_array: Vec<T> = Vec::with_capacity(right_array_size);

        for i in 0..left_array_size {
            left_array.push(data[i].clone());
        }

        for i in 0..right_array_size {
            right_array.push(data[i+q+1].clone());
        }

        let mut left_finger = 0;
        let mut right_finger = 0;
        let mut break_position = 0;
        for i in p..r{
                if left_array[left_finger] < right_array[right_finger] {
                    data[i] = left_array[left_finger].clone();
                    left_finger+=1;
                }else{
                    data[i] = right_array[right_finger].clone();
                    right_finger+=1;
                }
                if left_finger == left_array_size || right_finger == right_array_size {
                    break_position = i; 
                    break;
                }
        }
        if left_finger == left_array_size {
            for i in right_finger..right_array_size{
                data[break_position] = right_array[i].clone();
                break_position+=1;
            }
        }else  {
            for i in left_finger..left_array_size{
                data[break_position] = left_array[i].clone();
                break_position+=1;
            }
        }

    }
}



impl<T> Sort for MergeSort<T>
where T: PartialEq+PartialOrd+Clone
{
type Output = T;
fn sort(data: &mut Vec<T>){
    Self::mergesort(data, 0, data.len());
}
}

/// find the minimum among all the elements in array, then swap it with ith element 
/// minimum always start at the first position of starting loop 
struct SelectionSort<T: PartialEq+PartialOrd> (PhantomData<T>);

impl<T> Sort for SelectionSort<T>
where T: PartialEq+PartialOrd
{
type Output = T;
fn sort(data: &mut Vec<T>){
    for i in 0..data.len() {
        let mut current_minimum_pos = i;
        for j in i..data.len() {
            if data[j] < data[current_minimum_pos] {
                current_minimum_pos = j;
            }
        }
        data.swap(current_minimum_pos,i);
    }
}
}

/// Bubblesorting algorithm
/// Sorts by comparing against the adjacent elements
pub struct BubbleSort<T: PartialEq+PartialOrd> (PhantomData<T>);

impl<T> Sort for BubbleSort<T>
where T: PartialEq+PartialOrd
{
type Output = T;
fn sort(data: &mut Vec<T>){
    for i in 0..data.len()-1 {
        for j in 0..data.len()-i-1 {
            if data[j] > data[j+1] {
                data.swap(j,j+1);
            }
        }
    }
}
}




#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn bubble_sort() {
        let mut data =vec![6,5,4,3,2,1];
        BubbleSort::sort(&mut data);
        assert_eq!(data, vec![1,2,3,4,5,6])
    }

    #[test]
    fn selection_sort() {
        let mut data =vec![6,5,4,3,2,1];
        SelectionSort::sort(&mut data);
        assert_eq!(data, vec![1,2,3,4,5,6])
    }


    #[test]
    fn merge_sort() {
        let mut data =vec![8,12,4,3,2,1];
        MergeSort::sort(&mut data);
        assert_eq!(data, vec![1,2,3,4,8,12])
    }


    #[test]
    fn quick_sort() {
        let mut data =vec![8,12,4,3,2,1];
        QuickSort::sort(&mut data);
        assert_eq!(data, vec![1,2,3,4,8,12])
    }
}