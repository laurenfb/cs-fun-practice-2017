# # You are given an unsorted array with integers between
# 1 and 1,000,000. One integer is in the array twice.
# Determine which one. Extra fun: Do it without sorting.

def find_double_number(array)
  raise TypeError.new('input must be an array') if !array.is_a?(Array)
  numbers = {}
  array.each do |a|
    raise TypeError.new('array must contain numbers') if !a.is_a?(Fixnum)
    if !numbers[a]
      numbers[a] = true
    else
      return a
    end
  end
  return false
end

puts find_double_number([5,4,3,3,5,6,4,3,3,56,64,4,3])
