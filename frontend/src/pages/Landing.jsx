import { useState } from "react"

export default function Landing() {
  return (
    <>
      <div className="flex flex-col h-screen bg-dark-secondary">
      <div className="flex-none">

        <div className="navbar flex flex-row h-[10%] justify-between w-screen bg-dark-primary fixed top-0 z-50">
          <div className="text-dark-accent font-mono font-extrabold pl-[5%] flex flex-row justify-center items-center logo w-[10%]">
            <p className="text-3xl hover:text-4xl hover:duration-150">GoVYA</p>  
          </div>
          <div className="flex flex-row items-center gap-16 px-20 text-light-primary text-lg font-semibold">
            <p className="hover:underline">Login</p>
            <p className="">|</p>
            <p className="hover:underline">Register</p>
          </div> 
        </div>
        <div className="h-screen video-background relative">
          <video autoPlay loop muted className="absolute inset-0 w-full h-full object-cover">
            <source src="./../src/assets/video-2.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <div className="absolute inset-0 bg-dark-primary bg-opacity-[15%]"></div>
          <div className="w-1/2 text-light-primary flex flex-col justify-center items-center absolute inset-0 pr-[5%] ">
            <div className="group">
              <p className="text-5xl font-extrabold mb-4 group-hover:text-[3.2rem] group-hover:duration-150">Seamless <font className=" text-[#67d2ec]">Shipping,</font></p>
              <p className="text-5xl font-extrabold group-hover:text-[3.2rem] group-hover:duration-150">Instant <font className=" text-[#e7895d]">Connections</font></p>
            </div>
            <div>
            <hr className="border w-[22rem] border-light-primary mx-auto mt-[15%] mb-10"/>
            </div>
            <div className="w-3/5 flex flex-row ">
            <div className="flex flex-col justify-center items-center font-bold hover:text-[1.130rem] text-lg font-mono text-light-primary pr-[1%]">
              <p className=" text-center ">Experience a new level of <span className="text-highlight-secondary">efficiency </span>in<span className="text-highlight-secondary"> logistics</span>. Connect with top-tier carriers <span className="text-highlight-secondary">instantly</span>, ensuring your cargo reaches its <span className="text-highlight-secondary">destination</span> with <span className="text-highlight-secondary">speed</span> and precision.</p>
            </div>
            </div>

          </div>
          
        </div>
      </div>
      </div>
      <div className="flex-grow bg-light-primary">
      <div>
        <div className="flex flex-row justify-center items-center">
          <div className="text-dark-primary text-center text-3xl m-10">
            <p className="">Our Strengths, Which makes us</p>
            <p className="font-bold ">the most preferable moving brand</p>
          </div>
        </div>  
          <div className="text-dark-backplace font-serif font-medium">
            <div className="strength1 flex flex-row justify-center items-center gap-[15%]">
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">36+</p>
                <p className="text-3xl">Years of Trust</p>
                <p className="text-xl">Delivering Smiles Since 1987</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">98000+</p>
                <p className="text-3xl">Moves Annually</p>
                <p className="text-xl">Happily Across the World</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">2+</p>
                <p className="text-3xl">Million sq.feet</p>
                <p className="text-xl">Warehousing Space</p>
              </div>
            </div>
          </div>
            <div className="text-dark-backplace font-serif font-medium mt-10">
            <div className="strength1 flex flex-row justify-center items-center gap-[11%]">
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">3000+</p>
                <p className="text-3xl">Trained Manpower</p>
                <p className="text-xl">makes your move safe & on time</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">126+</p>
                <p className="text-3xl">Branches PAN India</p>
                <p className="text-xl">to cover 1264 destinations nationally</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <p className="text-dark-accent text-4xl font-bold">1200+</p>
                <p className="text-3xl">Vehicles</p>
                <p className="text-xl">for Every Segment and needs</p>
              </div>
          </div>
            </div>

        </div>
        <div>
          <div className="flex flex-row justify-center items-center">
            <div className="text-dark-primary text-center text-3xl m-10 mt-[5%]">
              <p className="font-bold ">OUR CORE SERVICES</p>
              <p className="text-xl">We specialize in performing solutions at</p>
            </div>
          </div>
          <div className="text-dark-backplace font-serif font-medium text-2xl">
            <div className="strength1 flex flex-row justify-center items-center gap-[5%]">
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/group.png" alt="" className=" w-[40%]"/>
                <p className="">International Moving</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/building.png" alt="" className=" w-[40%]"/>
                <p className="">Domestic Moving</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/box.png" alt="" className=" w-[40%]"/>
                <p className="">Removal & Storage</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/truckt.png" alt="" className=" w-[40%]"/>
                <p className="">Car Carriers</p>
              </div>
            </div>
            </div> 
            <div className="text-dark-backplace font-serif font-medium text-2xl m-10">
            <div className="strength1 flex flex-row justify-center items-center gap-[5%]">
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/dtruck.png" alt="" className=" w-[35%]"/>
                <p className="mt-1">Contract Logistics</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/forklift.png" alt="" className=" w-[35%]"/>
                <p className="mt-1">Commercial Moving</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/load.png" alt="" className=" w-[35%]"/>
                <p className="mt-1">Industrial Moving</p>
              </div>
              <div className="flex flex-col justify-center items-center">
                <img src="./../src/assets/warehouse.png" alt="" className=" w-[35%]"/>
                <p className="mt-1">Warehousing</p>
              </div>
              </div>
              </div>
            
            <div>
              <div className="flex flex-row justify-center items-center">
              <div className="text-dark-primary text-center text-3xl mt-8">
                <p className="font-bold ">FEATURED ON:</p>
              </div>
              </div>
              <div className="newslogos flex flex-row justify-center items-center gap-[8%]">
                <img src="./../src/assets/flogo1.png" alt="" />
                <img src="./../src/assets/flogo2.png" alt="" />
                <img src="./../src/assets/flogo4.png" alt="" />
                <img src="./../src/assets/flogo5.png" alt="" />
              </div>              
            </div> 

            <div className="pb-5"> 
              <div className="flex flex-row justify-center items-center">
              <div className="text-dark-primary text-center text-3xl mt-[4%] m-8">
                <p className="font-bold ">OUR CLIENTS:</p>
              </div>
              </div>
              <div className="newslogos flex flex-row w-screen justify-center items-center gap-[3%]">
                <img src="./../src/assets/airtel.png" alt="" />
                <img src="./../src/assets/apollo.png" alt="" />
                <img src="./../src/assets/asian-paints.png" alt="" />
                <img src="./../src/assets/godrej.png" alt="" />
                <img src="./../src/assets/havells.png" alt="" />
                <img src="./../src/assets/hyundai.png" alt="" />
                <img src="./../src/assets/pepsico.png" alt="" />
                <img src="./../src/assets/suzuki.png" alt="" />
                <img src="./../src/assets/tata.png" alt="" />

              </div>              
            </div>  
          </div>
      </div>

        <div className="contact flex flex-col w-screen h-[25%] bg-dark-secondary text-light-primary items-center bottom-0">
          <div className="w-[80%] flex flex-row text-justify m-10">
            <div className="w-1/3 flex flex-row justify-center">
              <div className="text-sm text-left">
                <p className="font-bold text-base">Contact Us :</p>
                <div className="">
                  <p><span className="italic pr-2">Address:  </span>GoVYA Packaging, Westind Country Club Rd, Industrial Area, Manipal, Karnataka - 576104</p>
                  <p><span className="italic pr-2">Email:  </span>govya@services.mail.com</p>
                  <p><span className="italic pr-2">Phone:  </span>+91 99876 56789</p>
                  <p><span className="italic pr-2">Telephone:  </span>+12 18432-232-423</p>
                </div>
              </div>
            </div>
            <div className="w-1/3 flex flex-row justify-center">
              <div className=""><div className="font-extrabold">
                <p>Disclaimer</p>
                </div>
                <div className="font-serif text-sm">
                  <p>Operational metrics listed are as of August 04, 2023. </p>
                  <p>GoVYA © ltd.</p>
                </div>
                <div className="font-serif text-sm m-5 flex flex-row justify-between">
                  <p className="hover:underline">Terms and Conditions</p>
                  <p>|</p>
                  <p className="hover:underline">Privacy Policy</p>
                </div>
              </div>
            </div>
            <div className="w-1/3 flex flex-row justify-center">
              <div className="text-justify">
                <p className="font-extrabold"> Information Security Policy</p>
                <p className="font-serif text-sm">GoVYA is committed to safeguarding the confidentiality, integrity and availability of all physical and electronic information assets of the organization.
We ensure that the regulatory, operational and contractual requirements are fulfilled.</p>
              </div>
            </div>
          </div>
        </div>
    </>
  )
}