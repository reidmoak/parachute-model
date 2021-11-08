#!/bin/bash

mod_list=`ls | grep -vE "__pycache__|README|\.sh"`

echo ""

for module in $mod_list; do
    cd $module
    echo -e "================================================================="
    echo -e "================================================================="
    echo -e "Running all tests in module \e[32;1m$module\e[0m\n"

    test_list=`find . -type f -name "*test.py"`
    if [[ -z $test_list ]]; then
        echo -e "No test cases for module $module\n"
    fi

    for test_case in $test_list; do
        base_case=`basename $test_case | sed 's/\.py//g'`
        echo -e "\nTest Case: ${base_case}\n"
        python -m tests.$base_case
    done
    cd ..
    echo -e "================================================================="
    echo -e "================================================================="
    echo -e "\n"
done

