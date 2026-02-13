import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Marin", page_icon="🌹", layout="centered")

def main():
    st.balloons()
    st.title("💐 Happy Valentine's Day Marin!")
    st.write("*(Tap the screen to grow more flowers!)*")

    # Interactive & Responsive 2D Animated Bouquet
    canvas_bouquet_code = """
    <div id="wrapper" style="width: 100%; display: flex; justify-content: center; background: #fffafa; border-radius: 20px; touch-action: none; cursor: crosshair; border: 1px solid #ffe4e1;">
        <canvas id="flowerCanvas"></canvas>
    </div>

    <script>
    const canvas = document.getElementById('flowerCanvas');
    const ctx = canvas.getContext('2d');
    const wrapper = document.getElementById('wrapper');
    
    function resize() {
        canvas.width = wrapper.offsetWidth;
        canvas.height = 400; 
    }
    resize();

    const flowers = [];
    const colors = ['#ff0a54', '#ff477e', '#ff7096', '#ff85a1', '#fbb1bd', '#e9edc9', '#ffcc00'];
    const centerX = canvas.width / 2;
    const baseY = canvas.height;

    class Flower {
        constructor(x, targetY, color, delay) {
            this.x = x;
            this.targetY = targetY;
            this.color = color;
            this.delay = delay;
            this.stemHeight = 0;
            this.bloomSize = 0;
            this.growthSpeed = 2 + Math.random() * 2;
            this.isBlooming = false;
            this.age = 0;
        }

        draw() {
            if (this.age < this.delay) return;
            const currentY = baseY - this.stemHeight;
            
            // Draw Stem
            ctx.beginPath();
            ctx.moveTo(centerX, baseY);
            ctx.quadraticCurveTo(centerX, baseY - 50, this.x, currentY);
            ctx.strokeStyle = '#3a5a40';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw Flower
            if (this.isBlooming) {
                ctx.fillStyle = this.color;
                for (let i = 0; i < 6; i++) {
                    ctx.beginPath();
                    ctx.ellipse(
                        this.x + Math.cos(i * Math.PI / 3) * this.bloomSize * 0.5,
                        currentY + Math.sin(i * Math.PI / 3) * this.bloomSize * 0.5,
                        this.bloomSize * 0.6, this.bloomSize * 0.4, (i * Math.PI / 3), 0, 2 * Math.PI
                    );
                    ctx.fill();
                }
                ctx.beginPath();
                ctx.arc(this.x, currentY, this.bloomSize * 0.3, 0, Math.PI * 2);
                ctx.fillStyle = '#ffb703';
                ctx.fill();
            }
        }

        update() {
            this.age++;
            if (this.age < this.delay) return;
            if (this.stemHeight < (baseY - this.targetY)) {
                this.stemHeight += this.growthSpeed;
            } else {
                this.isBlooming = true;
                if (this.bloomSize < 18) this.bloomSize += 0.8;
            }
        }
    }

    // Initial bouquet
    for (let i = 0; i < 20; i++) {
        addFlower(
            (canvas.width * 0.2) + Math.random() * (canvas.width * 0.6),
            (canvas.height * 0.1) + Math.random() * (canvas.height * 0.4),
            Math.random() * 50
        );
    }

    function addFlower(x, y, delay = 0) {
        const color = colors[Math.floor(Math.random() * colors.length)];
        flowers.push(new Flower(x, y, color, delay));
    }

    // Listen for clicks or touches
    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        addFlower(e.clientX - rect.left, e.clientY - rect.top, 0);
    });

    canvas.addEventListener('touchstart', (e) => {
        const rect = canvas.getBoundingClientRect();
        const touch = e.touches[0];
        addFlower(touch.clientX - rect.left, touch.clientY - rect.top, 0);
        e.preventDefault();
    }, {passive: false});

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        flowers.forEach(f => { f.update(); f.draw(); });
        requestAnimationFrame(animate);
    }
    animate();
    </script>
    """

    components.html(canvas_bouquet_code, height=420)

    st.markdown("---")
    
    # User Input and Interaction
    with st.expander("💌 Please open:"):
        st.write("I think you're really cool! 🌷")
        with st.expander("🌸 Keep Going"):
            st.write("I find you really pretty!")
            with st.expander("💌 Keep Going!"):
                st.write("I've enjoyed every single moment with you so far!")
                with st.expander("🌸 Keep Going!!"):
                    st.write("I want to keep seeing you!")
                    with st.expander("💌 Keep Going!!!"):
                        st.write("Alexa Marin Lim, I Like you! 林文晶, 我喜欢你!")
                        with st.expander("📝 Note:"):
                            st.write("Sorry for pussying out and telling you this way, but I hope you know that I really like you and I want to keep seeing you!")
       
if __name__ == "__main__":
    main()