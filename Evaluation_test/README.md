# Python Analysis Package for AWAKE
## Evaluation test for GSOC Project

Hi, here's the evaluation test for Python Analysis Package for AWAKE. 
> I studied & have been a research-based fan of modern physics from past 5 years from now. CERN is famous for its collider-oriented experiments with an emphasis on the “big” questions of particle physics. And, to get to contribute in AWAKE EXPERIMENT (proton-driven plasma accelerations) would be an unstoppable trigger for me to accomplish more robust scientific applications and quality code-base.


## Evaluation Test 

- images: export dir for required image(s)
- features: export dir for all dataset's meta-info in *.csv format
- data: remote hdf5 file is fetched into this directory


    ```
    conda create -n p3 python=3
    activate p3
    ```

    ```python
    pip install -r requirements.txt
    python main.py
    ```


![Execution Test](Capture.PNG)


## NOTE: 

Your project proposal should address two topics:

- AWAKE has tens of thousands of hdf files containing event data from the experiment. These files are "uneven" in that they do not all contain the same data. Propose a technique for creating a uniform, easily searchable database for AWAKE and writing an API that will allow AWAKE scientists to quickly search for and extract relevant data.


- Once the database has been created, you can contribute to the development of analysis tools for the AWAKE data. This can include image analysis and data visualization tools. There is also an opportunity to use machine learning algorithms to search for correlations in the data, but that is not a requirement for the project.

> Thanking you Dr. Gessner & GSOC for opportunity,\
Cheers

contact : wittycodes@gmail.com
