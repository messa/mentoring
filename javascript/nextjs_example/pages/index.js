import { useState } from "react"

function IndexPage() {

    const [ triggered, setTriggered ] = useState();

    setTimeout(() => {
        setTriggered(true);
    }, 2000);

    const styles = {}
    if (triggered) {
        styles.color = 'red'
    }
    return (
        <div>
            <h1>Hello</h1>
            <p style={styles}>
                První odstavec
            </p>
            {triggered && (
                <p>
                    This is new. {1 + 2}
                </p>
            )}
        </div>
    )
}

export default IndexPage
