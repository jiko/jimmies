#!/usr/bin/env ruby

require 'rubygems'
require 'chatterbot/dsl'

path = "/home/jk/Code/bots/jimmies/"

# http://stackoverflow.com/questions/11007111/ruby-whats-an-elegant-way-to-pick-a-random-line-from-a-text-file
def pick_random_line(file)
  chosen_line = nil
  File.foreach(file).each_with_index do |line, number|
    chosen_line = line if rand < 1.0/(number+1)
  end
  return chosen_line
end

#debug_mode and no_update

#verbose

# here's a list of users to ignore
# would like to automate adding people to this list if they freak out
# blacklist "abc", "def"

# here's a list of things to exclude from searches
exclude "unrustled", "thank", "thanks", "stop"

search "'my jimmies'", opts={:count => 1} do |tweet|
  reply "#USER# " + pick_random_line(path+"responses.txt"), tweet
end

replies do |tweet|
  reply "#USER# " + pick_random_line(path+"replies.txt"), tweet
end

tweet pick_random_line(path+"lines.txt")
