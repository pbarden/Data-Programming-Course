
require 'csv'

csv_contents = CSV.read('input.csv')

csv_contents.shift

puts 'Student      Assignment Average'
avg = 0.0
csv_contents.each do |col|
    avg =(col[1].to_f + col[2].to_f + col[3].to_f)/4.0

    puts col[0].to_s + " " + avg.to_s
end