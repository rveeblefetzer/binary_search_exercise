#!/usr/bin/env ruby
# A counter to show how many steps it takes to 
# find a number using binary search
# TODO: Do the numbers really need to be random? Or is a sequential array fine?
# Maybe take inputs, instead of hard-coded array size

puts "This is a quick and dirty program to show the efficiency of binary search."
puts "How big of a list do you want to search through?"
list_size = gets.chomp
if list_size.to_i > 1e6
  puts "OK, but this might take a while"
end
define_method :bin_search_counter do
  list = list_size.to_i.times.map{Random.rand(list_size.to_i)}.uniq.sort
  number = list[Random.rand(list.length)]
  low = 0
  high = list.length - 1
  counter = 1
  
  while low <= high
    mid = (low + high) / 2
    guess = list[mid]
    
    if guess == number
      break
    counter += 1
    end

    if guess > number
      high = mid - 1
      counter += 1
    else
      low = mid + 1
      counter += 1
    end
  end

  puts "-" * 20
  puts "This is a quick and dirty program to show the efficiency of binary search."
  puts "The number to look up was: #{number}"
  puts
  puts "It was one entry in a list of #{list.length} random, unique numbers."
  puts 
  puts "Binary search found the item in #{counter} tries."
  puts "The Big O notation for this search was O(log #{list.length}), or O(" + Math.log(list.length, 2).to_s + ")"
  puts "*"  * 20
end

bin_search_counter
