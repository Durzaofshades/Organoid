#!/bin/bash

# in the terminal run reformat on a folder to sort each file based on name

target="$1"

(
  cd $target

  treatment=("Candin" "Casta" "Mock" "PIC" "LPS")
  donor=("Donor 1" "Donor 2" "Donor 3" "Donor 4" "Donor 5")
  time=("12hr" "24hr" "48hr")
  size=("5x" "20x" "40x")

  IFS=$'\n'

  for t in ${treatment[@]}; do
    printf "$t \n"
    
    # Make the Treatment Directory
    mkdir -p $t

    # find any files with the treatment in the name
    files=$(find ./ -iname "*$t*")

    # loop over files
    for f in $files; do
      mv $f $t
    done

    (
      cd $t
        for d in ${donor[@]}; do
        # Make Directory
        mkdir -p $d

        files=$(find ./ -iname "*$d*")
        for f in $files; do
          mv $f $d
        done

        ( cd $d
          for h in ${time[@]}; do
          # Make Directory
          mkdir -p $h

          files=$(find ./ -iname "*$h*")
          for f in $files; do
            mv $f $h
          done

          ( cd $h
            for m in ${size[@]}; do
            # Make Directory
            mkdir -p $m

            files=$(find ./ -iname "*$m*")
            for f in $files; do
              mv $f $m
            done

          done
          )
        done
        )
      done
    )
  done
)

find ./ -iname "*.tif"

echo "Finished"
