

#SubGen: Subdomain Generation with GAN-based Machine Learning

## **Introduction**  
SubGen is an advanced machine learning project designed to generate subdomains intelligently using GAN. This project leverages the power of GANs to predict potential subdomains for a given domain, enhancing the capabilities of penetration testers, bug bounty hunters, and cybersecurity professionals.  

By analyzing existing subdomain patterns, SubGen predicts new subdomains that might exist but are not yet discovered, offering an innovative approach to reconnaissance and attack surface enumeration.

---


#### **Why SubGen?**  
1. 🌍 **Cutting-Edge Technology**: Combines state-of-the-art GAN architecture with domain-specific intelligence.  
2. 🚀 **Comprehensive Recon Tool**: Streamlines subdomain discovery with unmatched accuracy and flexibility.  
3. 🧠 **AI-Driven Predictions**: Utilizes adversarial machine learning to predict potential subdomains, staying ahead of traditional tools.  


---

## **Features**  
SubGen provides an advanced solution for subdomain enumeration using GAN-based machine learning, offering exceptional customization and intelligence.  

### **1. Adjustable Subdomain Levels**
- 🎯 **Granular Control**: Specify the depth of subdomain generation with the `--level` parameter. Choose from a wide range of levels (exam 1-5) to determine the complexity and depth of generated subdomains.  
- 🧩 **Customizable Enumeration**: Enables targeted discovery of subdomains for deep or shallow reconnaissance, based on user needs.  

### **2. Pattern Combination Based on TLD**
- 🔗 **TLD-Aware Generation**: Leverages patterns and conventions associated with specific Top-Level Domains (TLDs) such as `.com`, `.org`, `.edu`, etc.  
- 🔍 **Enhanced Accuracy**: Generates subdomains that align closely with the naming conventions and structural patterns typically used under the given TLD.  
- 🌐 **Wide Applicability**: Optimized for diverse TLDs, making it suitable for global reconnaissance efforts.  

### **3. Intelligent Domain Logic**
- 🌐 **Domain Intelligence**: Creates realistic subdomains based on learned patterns from existing domain structures.  
- 🚀 **Customizable Process**: Fine-tune the generation process with user-defined parameters such as depth levels, wordlists, and existing subdomain lists.  

### **4. Seamless Workflow**
- 🛠️ **Integrated Workflow**: Supports custom input files for words and subdomains, making it adaptable for various use cases.  
- 💾 **Flexible Output**: Exports results to specified output files for easy integration with other tools or workflows.  

### **5. Smart Wordlist Integration**
- 📜 **Dynamic Wordlist Usage**: Incorporates user-provided wordlists (`-w`) and known subdomains (`-sub`) to enhance the accuracy of predictions.  
- 🤖 **Pattern Learning**: Trains the GAN model to generate subdomains that closely match the linguistic patterns found in your wordlist.  

### **6. Context-Aware Subdomain Generation**
- 🌟 **Domain-Specific Learning**: Analyzes existing subdomains and applies learned patterns to produce realistic results tailored to the target domain.  
- 🔧 **Customization Options**: Fine-tune the generation process using multiple input parameters for specific needs.  

### **7. Scalable Output and Export**
- 💾 **Flexible Export**: Save results in the desired format with the `-o` parameter, making it easy to integrate with other tools.  
- 📊 **Batch Processing**: Handles large-scale domains with ease, offering efficient enumeration for enterprise use cases.  

### **8. Performance and Efficiency**
- ⚡ **Optimized Computation**: Uses cutting-edge GAN technology to deliver high-quality subdomains without compromising speed.  
- 🔄 **Iterative Refinement**: Continuously improves subdomain predictions through adversarial training of generator and discriminator networks.  


---

## **How It Works**  
SubGen employs a **GAN-based machine learning algorithm** where two neural networks, the generator and discriminator, compete against each other.  
1. **Generator**: Creates potential subdomain names based on learned patterns.  
2. **Discriminator**: Evaluates the validity of generated subdomains against real-world patterns.  
This adversarial process continues until the generator produces high-quality, realistic subdomains.  

---

## **Usage**  
### **Command-Line Interface**  
Run the tool using the following command:  
```bash  
python3 main.py -u <domain> -w <wordlist> -sub <subdomain_list> --level <range> -o <output_file> [-h]
```  

### **Example**  
```bash  
python3 main.py -u site.com -w words.txt -sub sub.txt --level 1-5 -o output.txt -h  
```  

### **Parameters**  
- `-u`: Specify the target domain (e.g., `example.com`).  
- `-w`: Provide a wordlist file for generating subdomains.  
- `-sub`: Include a list of known subdomains for pattern analysis.  
- `--level`: Define the depth level for subdomain generation (e.g., `1-5`).  
- `-o`: Specify the output file to save results.  
- `-h`: Display help and usage information.  

---


### **Installation**  
Before running the project, make sure to install the required dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

### **Requirements**
- Python 3.8+  
- Libraries:
  - `torch`: For building and training GAN models.
  - `tldextract`: For parsing and extracting domain and TLD information.

---



### **Installation** 
1. Clone the repository:  
   ```bash  
   git clone https://github.com/0x0F1x/SubGen.git  
   cd SubGen  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## **Applications**  
- Cybersecurity: Expand your attack surface by discovering hidden subdomains.  
- Bug Bounty: Enhance your reconnaissance workflow for maximum impact.  
- Red Teaming: Uncover subdomain structures that could lead to vulnerabilities.  
- Research: Leverage machine learning for domain pattern analysis.  

---

## **Contributing**  
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to help improve SubGen.  

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  



---

### **Donate**  
SubGen is an open-source project that relies on community support and donations to continue growing and improving. If you're benefiting from this project and would like to support it, please consider making a donation.

🧡 **Support the Project**    
- **BTC**:  [bc1qhkfen9qrj6l5d5p3e50jyxc2whffr03estfr37](#)
- **ETH**:  [0xDCB274A50a86399d451f537ba857799DC8D3fED8](#)
- **XRP**:  [rPNJ5DN37NKCCtzgMEcA7eSgJXaCE6uUzR](#)
- **XMRT**:  [0x7f7Fba841Eb9f6cE80F1968298c558dC0a2e5a5f](#)
- **USDTet**:  [terra1xakltt4zacem7795cxug3su5end6299h347skg](#)
- **USDT(ETH)**:  [0xDCB274A50a86399d451f537ba857799DC8D3fED8](#)
- **USDT(tron)**:  [TMDsCUiAEzPvS7MzzV9BoCmF5FY9NGmvmN](#)
- **LTC**:  [ltc1qg9zqymcv63v3ccmh3fm2ak2y7vdsftn0xse2ky](#)
Your donations allow us to add new features, fix bugs, and make SubGen an even more powerful tool for the cybersecurity community.

---

 
👋 **Thank you for trying out SubGen!**  
We truly appreciate your support in expanding this project. Your feedback, suggestions, and contributions are highly valued. If you have any questions or need assistance, we’re here to help. Please share this project with others and consider supporting us if possible.

**By using SubGen, you’re advancing the field of cybersecurity and contributing to the growth of knowledge in penetration testing and network data gathering.**

---








