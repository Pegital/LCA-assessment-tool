# LCA-assessment-tool
computational tool that bridges the Oekobaudat API with Grasshopper, By automating LCA data retrieval and analysis, the tool empowers designers to evaluate environmental metrics such as global warming potential (GWP) and energy consumption in real time eco-conscious decision-making during the conceptual design phase. 

The tool was developed using a three-stage workflow. First, the Oekobaudat API was integrated via Python scripting in Grasshopper to query material-specific environmental data (e.g., CO₂eq per kilogram of concrete or steel). API endpoints were accessed using requests, with JSON responses parsed into Grasshopper-readable formats. Second, a user interface was designed within Grasshopper, featuring customizable input parameters (e.g., material type).  

The tool successfully automates LCA workflows, reducing calculation time compared to manual methods. 

 

System Overview 

The developed LCA tool enables users to select materials interactively, retrieve environmental impact data via API calls, and calculate the GWP based on geometry inputs. The tool integrates several key functionalities: 

Material Selection: Users choose materials from a categorized list. 

UUID Extraction: The system retrieves the unique identifier (UUID) for the selected material. 

GWP Data Retrieval: The API is called using the UUID to obtain environmental impact values. 

Geometry-Based Calculations: Users input one or multiple geometries, which are analyzed based on material-specific units. 

Unit Extraction for Accurate Calculation: The tool determines whether to calculate GWP by surface area or volume, depending on the material type. 

Backend Development with Python 

The backend of the LCA tool is built in Python, handling API interactions, data processing, and calculations. The key steps involved in the backend development include: 

1. API Integration 

The Okobaudat API provides environmental data for construction materials. To obtain the GWP values: 

The system first retrieves a list of materials categorized by type. 

Upon user selection, the corresponding UUID is extracted. 

The UUID is used in an API call to fetch the GWP value. 

 
 
 

2. Unit Extraction and Calculation 

Since different materials have different unit bases (e.g., square meters vs. cubic meters), the system determines the appropriate calculation method: 

Frontend Development with Human UI 

The frontend, built using Human UI, allows users to: 

Browse and select materials from categorized lists. 

View material details and GWP values. 

Input geometry data. 

Receive real-time LCA calculations. 

Human UI provides a graphical interface within Rhino/Grasshopper, making it an intuitive choice for designers. 
