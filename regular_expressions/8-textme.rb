#!/usr/bin/env ruby
log_line = ARGV[0]
result = log_line.match(/from:(?<from>.*?)\].*?to:(?<to>.*?)\].*?flags:(?<flags>.*?)\]/)
puts "#{result[:from]},#{result[:to]},#{result[:flags]}" if result
