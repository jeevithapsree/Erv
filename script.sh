#!/bin/bash

while true; 


do aws sagemaker stop-notebook-instance --notebook-instance-name 'erv-instance';

done;

do aws sagemaker delete-notebook-instance --notebook-instance-name 'erv-instance';

done;
