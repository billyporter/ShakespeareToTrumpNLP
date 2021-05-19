# ShakespeareToTrumpNLP

## Files
### The main results are in Trump_fake_3
    .
    ├── data
    │    ├── shakespeare  
    │    │   ├── alllines.txt.txt                         # All Shakespeare Lines 
    │    │   ├── clean_modern.txt                         # Modern Shakespeare lines before tokenizing
    │    │   ├── clean_original.txt                       # Original Shakespeare lines before tokenizing
    │    │   └── processed
    │    │        ├── all_proc.txt                        # All Lines after cleaning and tokenizing
    │    │        ├── modern_proc.txt                     # Modern Shakespeare lines after tokenizing
    │    │        └── original_proc.txt                   # Original Shakespeare lines after tokenizing
    │    └── trump
    │    │        ├── speeches
    │    │        │    ├── cln_speech.txt
    │    │        │    └── speech.txt
    │    │        └── tweets 
    │    │             ├── cln_tweets.txt 
    │    │             ├── tweets.json.tx
    │    │             └── tweets_01-08-2021.csv.txt
    └──src                    
         ├── baseline 
         │    └── baseline.py                              # Creates baseline model
         ├── cleaning   
         │    ├── shake_cleaning.py                        # Cleans and tokenizes Shakespeare lines
         │    └── trump_cleaning.py                        # Cleans and tokenizes Trump tweets and speeches
         └── model_hw2
             ├── data
             │    ├── s_to_t
             │    │    └── shake_fake_1                     # Pseudo Shakespeare data produced by IBT
             │    ├── t_to_s
             │    │    └── trump_fake_1                     # Psuedo Trump data produced by IBT 
             │    ├── temp_combine.txt                      # Temporary total combined data of (source, target) (100%)
             │    ├── temp_dev.txt                          # Temporary combined dev data of (source, target) for training (80%)
             │    ├── temp_train.txt                        # Temporary total combined data of (source, target) (20%)
             │    └── truth
             │        ├── all_proc.txt                     # Copied from data/shakespeare/processed/
             │        ├── modern_proc.txt                  # Copied from data/shakespeare/processed/
             │        ├── original_proc.txt                # Copied from data/shakespeare/processed/
             │        └── trump.txt                        # Combined Trump tweets and speeches
             ├── driver.py                                 # Main file to run IBT process
             ├── layers.py                                 # HW2 Layers for NMT
             ├── output.txt                                # Trainer output for some of the epochs
             ├── transformer.py                            # Modified HW2 Transformer for GPU
             └── saved_models   
                 ├── model_ST_1                            # IBT Process Shakespeare to Trump Model
                 └── model_TS_1                            # IBT Process Trump to Shakespeare

## Instructions
To start the IBT process run:
   python3 src/model_hw2/driver.py
